import streamlit as st
import folium
from streamlit_folium import folium_static
import json

def main():
    trayek = []
    halte = []
    st.title("Perancangan Trayek Angkot Pungkot (Lampung Angkot)")
    st.image("https://thumb.viva.co.id/media/frontend/thumbs3/2022/07/15/62d12e3508826-angkot_665_374.jpg")
    geojson_path = "trayek.geojson"  # Update the path accordingly
    with open(geojson_path, 'r') as file:
        geojson_data = json.load(file)
    for geo in geojson_data["features"]:
        types = geo["geometry"]["type"]
        if types == "Point":
            point = geo["geometry"]["coordinates"]
            point[0],point[1]=point[1],point[0]
            del point[2]
            halte.append({"location":point,"popup": geo["properties"]["name"]})
        elif types == "LineString":
            coordinate = geo["geometry"]["coordinates"]
            print("DAMN")
            for c in coordinate:
                c[0], c[1] = c[1], c[0]
                del c[2]
            trayek.append(coordinate)

    # Create a map centered at a specific location
    m = folium.Map(location=[-5.358893830037456, 105.3162627551661], zoom_start=15)

    pilihTrayek = st.selectbox("Trayek Angkot",options=["Angkot 1","Angkot 2","Semua Angkot"])
    if pilihTrayek == "Angkot 1":
       st.write("Trayek: KOTABARU - BELWIS - PEMDA - AIRAN - ITERA")
       st.write("Pemberhentian: 6 Halte")
       st.write("Warna Angkot: Merah")
       line_route = folium.PolyLine(
           locations=trayek[0],
           color='red',
           weight=5,
           opacity=0.7,
       ).add_to(m)
    elif pilihTrayek == "Angkot 2":
       st.write("Trayek: KOTABARU - ITERA - SUKARAME - UIN")
       st.write("Pemberhentian: 6 Halte")
       st.write("Warna Angkot: Biru")
       line_route = folium.PolyLine(
           locations=trayek[1],
           color='blue',
           weight=5,
           opacity=0.7,
       ).add_to(m)

    else:
    	line_route = folium.PolyLine(
           locations=trayek[0],
           color='red',
           weight=5,
           opacity=0.7,
       ).add_to(m)
    	line_route = folium.PolyLine(
           locations=trayek[1],
           color='blue',
           weight=5,
           opacity=0.7,
       ).add_to(m)

    points = halte
    for point in points:
        folium.Marker(
            location=point["location"],
            popup=point["popup"],
            icon=folium.Icon(color='green')
        ).add_to(m)

    # Render the map
    folium_static(m)

    st.markdown("---")
    st.write("Credit:")
    st.write("Virdio Samuel Saragih - 122450124")
    st.write("Haikal Dwi Syaputra - 122450067")
    st.write("Baruna Abirawa - 122450097")
    st.write("Danang Hilal Kurniawan - 122450085")

if __name__ == "__main__":
    main()
