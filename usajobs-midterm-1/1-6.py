import requests

url = "https://data.usajobs.gov/api/jobs"
states = ['California', 'Florida', 'Maryland', 'New York']
state_data = list()
state_data += [["State", "Job Count"]]

for s in states:
  atts = {'CountrySubdivision': s, 'NumberOfJobs': 1}
  response = requests.get(url, params = atts)
  jobs = int(response.json()['TotalJobs'])
  state_data += [[s, jobs]]

chartcode = """
<!DOCTYPE html>
<html>
  <head>
    <title>Sample Chart</title>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
  </head>
  <body>
    <script type="text/javascript">
      google.load("visualization", '1.1', {packages:['corechart']});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = %s
        var datatable = google.visualization.arrayToDataTable(data);
        var options = {
          width: 600,
          height: 400,
          legend: { position: 'none' },
        };
        var chart = new google.visualization.BarChart(document.getElementById('mychart'));
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

htmlfile = open("1-6.html", "w")
htmlfile.write(chartcode % state_data)
htmlfile.close()