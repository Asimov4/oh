AmCharts.ready(function () {

    function parseDate() {
        for( var i = 0; i < chartData.length; ++i )
            chartData[i]["data"]["upload_date"] =  new Date(chartData[i]["data"]["upload_date"]);
        return chartData;
        }

        // SERIAL CHART
        chart = new AmCharts.AmSerialChart();
        chart.pathToImages = "../amcharts/images/";
        chart.zoomOutButton = {
            backgroundColor: '#000000',
            backgroundAlpha: 0.15
        };
        chart.dataProvider = chartData;
        chart.categoryField = "date";

        // listen for "dataUpdated" event (fired when chart is inited) and call zoomChart method when it happens
        chart.addListener("dataUpdated", zoomChart);

        // AXES
        // category
        var categoryAxis = chart.categoryAxis;
        categoryAxis.parseDates = true; // as our data is date-based, we set parseDates to true
        categoryAxis.minPeriod = "DD"; // our data is daily, so we set minPeriod to DD
        categoryAxis.dashLength = 2;
        categoryAxis.gridAlpha = 0.15;
        categoryAxis.axisColor = "#DADADA";


        var i = 0;
        for (var key in chartData[0]) {
            if (key != 'date') {
                var valueAxis = new AmCharts.ValueAxis();
                valueAxis.offset = i * 40;
                valueAxis.dashLength = 4;
                valueAxis.axisColor = "#FF6600";
                valueAxis.axisAlpha = 0;
                chart.addValueAxis(valueAxis);

                // GRAPH
                var graph = new AmCharts.AmGraph();
                graph.valueAxis = valueAxis; // we have to indicate which value axis should be used
                graph.type = "line";
                graph.title = "infection # " + i;
                graph.valueField = key;

                graph.customBullet = "images/star.gif"; // bullet for all data points
                graph.bulletSize = 14; // bullet image should be a rectangle (width = height)
                graph.customBulletField = "customBullet"; // this will make the graph to display custom bullet (red star)
                chart.addGraph(graph);
            }
            i = i + 1;
        }


        // CURSOR
        var chartCursor = new AmCharts.ChartCursor();
        chartCursor.cursorPosition = "mouse";
        chart.addChartCursor(chartCursor);

        // SCROLLBAR
        var chartScrollbar = new AmCharts.ChartScrollbar();
        chart.addChartScrollbar(chartScrollbar);

        // LEGEND
        var legend = new AmCharts.AmLegend();
        legend.marginLeft = 110;
        chart.addLegend(legend);

        // WRITE
        chart.write("chartdiv");
});
