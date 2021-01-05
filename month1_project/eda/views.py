from django.http.response import HttpResponse
from django.shortcuts import render
from .models import NetflixData
import pandas as pd
import plotly.express as px
from plotly.offline import plot
import csv

# Create your views here.
def index(request):

    return render(request, "index.html", {})


# def Netflix_view(request):

# df = pd.DataFrame(columns=["Country", "Series_Count"])
# df["Country"] = [
#     "United States",
#     "India",
#     "United Kingdom",
#     "Canada",
#     "France",
#     "Japan",
#     "Spain",
#     "South Korea",
#     "Germany",
#     "Mexico",
# ]
# df["Series_Count"] = [2610, 838, 602, 318, 271, 231, 178, 162, 151, 129]
# df["continent"] = [
#     "Americas",
#     "Asia",
#     "Europe",
#     "Americas",
#     "Europe",
#     "Asia",
#     "Europe",
#     "Asia",
#     "Europe",
#     "Americas",
# ]
# df["code"] = ["USA", "IDN", "GBR", "CAN", "GUF", "JPN", "ESP", "KOR", "DEU", "MEX"]
# df["rank"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# fig = px.scatter_geo(
#     df,
#     locations="code",
#     text="rank",
#     color="continent",
#     hover_name="Country",
#     size="Series_Count",
#     projection="natural earth",
# )

# # pic = plot(fig, auto_open=False, output_type="div")
# # context["graph"] = pic
# graph = fig.to_html(full_html=False, default_height=500, default_width=700)
# context = {"graph": graph}
# response = render(request, "index.html", context)
