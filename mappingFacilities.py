# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:57:29 2025

@author: Admin
"""

import folium

# 2) Our existing dataset
facilities_data = [
    {
        "name": "1) Экибастузская ГРЭС-1 им. Б. Нуржанова",
        "old_price": 8.27,
        "new_price": 9.50,
        "lat": 51.8880,   # Approx. near Ekibastuz
        "lon": 75.3500,
        "capacity": "4,000 MW"
    },
    {
        "name": "2) Евроазиатская энергетическая корпорация (ЕАЭК)",
        "old_price": 7.98,
        "new_price": 9.40,
        "lat": 52.0404,   # Approx. near Aksu, Pavlodar Region
        "lon": 76.9273,
        "capacity": "2,500 MW"
    },
    {
        "name": "3) Станция Экибастузская ГРЭС-2",
        "old_price": 13.17,
        "new_price": 15.67,
        "lat": 51.6696,  # Another location near Ekibastuz
        "lon": 75.3620,
        "capacity": "2,000 MW"
    },
    {
        "name": "4) ГРЭС Топар (Главная распределительная энергостанция)",
        "old_price": 15.32,
        "new_price": 20.84,
        "lat": 49.3856,   # Approx. near Topar, Karaganda Region
        "lon": 75.7258,
        "capacity": "600 MW"
    },
    {
        "name": "5) Жамбылская ГРЭС им. Т.И. Батурова",
        "old_price": 17.73,
        "new_price": 22.58,
        "lat": 42.9140,   # Approx. in Zhambyl Region
        "lon": 71.3631,
        "capacity": "1,200 MW"
    },
    {
        "name": "6) Караганда Энергоцентр",
        "old_price": 14.09,
        "new_price": 17.64,
        "lat": 49.7513,  # Approx. in Karaganda
        "lon": 73.0943,
        "capacity": "650 MW"
    },
    {
        "name": "7) Усть-Каменогорская ТЭЦ",
        "old_price": 14.27,
        "new_price": 17.82,
        "lat": 49.9643,   # Approx. in Oskemen
        "lon": 82.6150,
        "capacity": "500 MW"
    },
    {
        "name": "8) Севказэнерго (Петропавловская ТЭЦ-2)",
        "old_price": 18.61,
        "new_price": 23.17,
        "lat": 54.8736,   # Approx. Petropavl
        "lon": 69.1290,
        "capacity": "900 MW"
    },
    {
        "name": "9) АО \"Астана-Энергия\"",
        "old_price": 9.28,
        "new_price": 11.71,
        "lat": 51.1897,   # Approx. Astana
        "lon": 71.4653,
        "capacity": "1,100 MW"
    },
    {
        "name": "10) \"Павлодарэнерго\" (ТЭЦ-2,3)",
        "old_price": 18.25,
        "new_price": 24.29,
        "lat": 52.3080,   # Approx. Pavlodar
        "lon": 76.9393,
        "capacity": "1,300 MW"
    },
    {
        "name": "12) АО \"Алюминий Казахстана\"",
        "old_price": 7.87,
        "new_price": 8.52,
        "lat": 52.2263,   # Pavlodar Aluminium Plant
        "lon": 76.8802,
        "capacity": "400 MW"
    },
    {
        "name": "13) \"Казахмыс Энерджи\" (ЖТЭЦ, БТЭЦ)",
        "old_price": 21.42,
        "new_price": 30.24,
        "lat": 47.7906,   # Approx. Zhezkazgan
        "lon": 67.7148,
        "capacity": "850 MW"
    },
    {
        "name": "16) \"Bassel Group LLS\"",
        "old_price": 16.73,
        "new_price": 25.48,
        "lat": 42.3174,   # Approx. near Shymkent
        "lon": 69.5901,
        "capacity": "550 MW"
    },
    {
        "name": "18) \"Степногорская ТЭЦ\"",
        "old_price": 28.97,
        "new_price": 38.67,
        "lat": 52.3452,
        "lon": 71.8853,
        "capacity": "400 MW"
    },
    {
        "name": "22) ГКП \"Кентау Сервис\"",
        "old_price": 7.07,
        "new_price": 37.12,
        "lat": 43.5161,   # Kentau, Turkestan Region
        "lon": 68.5042,
        "capacity": "300 MW"
    },
    {
        "name": "23) ГКП \"Аркалыкская ТЭК\"",
        "old_price": 8.44,
        "new_price": 13.13,
        "lat": 50.2525,   # Arkalyk, Kostanay Region
        "lon": 66.9132,
        "capacity": "250 MW"
    },
    {
        "name": "26) \"Алматинские электрические станции\" (ТЭЦ-1,2,3, Капшагайская ГЭС)",
        "old_price": 17.82,
        "new_price": 20.93,
        "lat": 43.2643,   # Almaty
        "lon": 76.9558,
        "capacity": "1,700 MW"
    }
]

# 3) Compute percentage increase
for f in facilities_data:
    old_ = f["old_price"]
    new_ = f["new_price"]
    f["pct_increase"] = (new_ - old_) / old_ * 100

# 4) Define a function to bin percentage increases
def get_group_by_percentage(pct):
    """
    Return an integer group (1..5) based on the pct_increase.
    We'll interpret them as:
      1: 0% - 20%
      2: 20% - 40%
      3: 40% - 60%
      4: 60% - 100%
      5: >100%
    """
    if pct <= 20:
        return 1
    elif pct <= 40:
        return 2
    elif pct <= 60:
        return 3
    elif pct <= 100:
        return 4
    else:
        return 5

# 5) Map color for each group
group_colors = {
    1: "blue",
    2: "green",
    3: "orange",
    4: "red",
    5: "purple"
}

# 6) Create the Folium map
m = folium.Map(location=[48.0, 68.0], zoom_start=5)

# 7) Add markers for each facility
for f in facilities_data:
    pct_increase = f["pct_increase"]
    group_id = get_group_by_percentage(pct_increase)
    color = group_colors[group_id]

    popup_html = (f"<b>{f['name']}</b><br>"
                  f"Capacity: {f['capacity']}<br>"
                  f"Old Price: {f['old_price']} тг/кВт·ч<br>"
                  f"New Price: {f['new_price']} тг/кВт·ч<br>"
                  f"Increase: {pct_increase:.2f}%")

    folium.Marker(
        location=[f["lat"], f["lon"]],
        popup=popup_html,
        tooltip=f["name"],
        icon=folium.Icon(color=color, icon="info-sign")
    ).add_to(m)

# 8) Create a custom legend
legend_html = """
     <div style="position: fixed;
     bottom: 50px; left: 50px; width: 200px; height: 175px;
     border:2px solid grey; z-index:9999; font-size:14px;
     background-color: white;
     padding: 5px;
     ">
     <b>Tariff Increase (%)</b><br>
     <i class="fa fa-map-marker fa-2x" style="color:blue"></i>
         &nbsp; 0 - 20%<br>
     <i class="fa fa-map-marker fa-2x" style="color:green"></i>
         &nbsp; 20 - 40%<br>
     <i class="fa fa-map-marker fa-2x" style="color:orange"></i>
         &nbsp; 40 - 60%<br>
     <i class="fa fa-map-marker fa-2x" style="color:red"></i>
         &nbsp; 60 - 100%<br>
     <i class="fa fa-map-marker fa-2x" style="color:purple"></i>
         &nbsp; > 100%
     </div>
"""

# Add the custom legend to the map
m.get_root().html.add_child(folium.Element(legend_html))

# 9) Display the map
m
m.save("electricityFacilitiesKZ.html")
