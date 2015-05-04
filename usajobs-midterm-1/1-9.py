import requests
import json

url = "https://data.usajobs.gov/api/jobs"
iso = json.loads(requests.get('http://stash.compjour.org/data/usajobs/us-statecodes.json').text)
states = [iso.keys()]
state_data = list()
state_data += [["State", "Job Count"]]

for s in iso.keys():
  atts = {'CountrySubdivision': s, 'NumberOfJobs': 1}
  response = requests.get(url, params = atts)
  jobs = int(response.json()['TotalJobs'])
  iso_code = "US-" + iso[s]
  state_data += [[iso_code, jobs]]

  chartcode = """
<html>
  <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
  </head>
  <body>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["geochart"]});
      google.setOnLoadCallback(drawRegionsMap);
      function drawRegionsMap() {
        var data = %s
        var datatable = google.visualization.arrayToDataTable(data);
        var options = {'region': 'US', 'width': 600, 'height': 400, 'resolution': 'provinces'};
        var chart = new google.visualization.GeoChart(document.getElementById('mychart'));
        chart.draw(datatable, options);
      }
    </script>
      <div class="container">
        <h1 style="text-align:center">Hello chart</h1>
        <div id="mychart"></div>
      </div>
  </body>
</html>
"""

htmlfile = open("1-9.html", "w")
htmlfile.write(chartcode % state_data)
htmlfile.close()