var chart;
var chartData = [];
var chartCursor;

// generate some random data, quite different range
function generateChartData() {
    var firstDate = new Date();
    firstDate.setDate(firstDate.getDate() - 500);

    for (var i = 0; i < chartDataEmotion.length; i++) {
        chartData.push({
            date: new Date(chartDataEmotion[i].upload_date),
            fearful: parseInt(chartDataEmotion[i].fearful, 10),
            angry: parseInt(chartDataEmotion[i].angry, 10),
            sad: parseInt(chartDataEmotion[i].sad, 10),
            happy: parseInt(chartDataEmotion[i].happy, 10)})};
}

// creat chart
AmCharts.ready(function() {
    // generate some data
    generateChartData();

    // SERIAL CHART
    chart = new AmCharts.AmSerialChart();
    chart.autoMarginOffset = 5;
    chart.marginBottom = 0;
    chart.pathToImages = "http://www.amcharts.com/lib/images/";
    chart.zoomOutButton = {
        backgroundColor: '#000000',
        backgroundAlpha: 0.15
    };
    chart.dataProvider = chartData;
    chart.categoryField = "date";
    chart.balloon.bulletSize = 5;

    // listen for "dataUpdated" event (fired when chart is rendered) and call zoomChart method when it happens
    chart.addListener("dataUpdated", zoomChart);

    // AXES
    // category
    var categoryAxis = chart.categoryAxis;
    categoryAxis.parseDates = true; // as our data is date-based, we set parseDates to true
    categoryAxis.minPeriod = "ss"; // our data is daily, so we set minPeriod to DD
    categoryAxis.dashLength = 1;
    categoryAxis.gridAlpha = 0.15;
    categoryAxis.position = "top";
    categoryAxis.axisColor = "#DADADA";

    // value
    var valueAxis = new AmCharts.ValueAxis();
    valueAxis.axisAlpha = 0;
    valueAxis.dashLength = 1;
    chart.addValueAxis(valueAxis);

    // GRAPH
    var graph = new AmCharts.AmGraph();
    graph.title = "fearful %";
    graph.valueField = "fearful";
    graph.bullet = "round";
    graph.bulletBorderColor = "#FFFFFF";
    graph.bulletBorderThickness = 2;
    graph.lineThickness = 2;
    graph.lineColor = "#000000";
    graph.negativeLineColor = "#efcc26";
    graph.hideBulletsCount = 50; // this makes the chart to hide bullets when there are more than 50 series in selection
    chart.addGraph(graph);

    // GRAPH
    var graph1 = new AmCharts.AmGraph();
    graph1.title = "angry %";
    graph1.valueField = "angry";
    graph1.bullet = "round";
    graph1.bulletBorderColor = "#FFFFFF";
    graph1.bulletBorderThickness = 2;
    graph1.lineThickness = 2;
    graph1.lineColor = "#ff0000";
    graph1.negativeLineColor = "#efcc26";
    graph1.hideBulletsCount = 50; // this makes the chart to hide bullets when there are more than 50 series in selection
    chart.addGraph(graph1);

    // GRAPH
    var graph2 = new AmCharts.AmGraph();
    graph2.title = "happy %";
    graph2.valueField = "happy";
    graph2.bullet = "round";
    graph2.bulletBorderColor = "#FFFFFF";
    graph2.bulletBorderThickness = 2;
    graph2.lineThickness = 2;
    graph2.lineColor = "#00ff00";
    graph2.negativeLineColor = "#efcc26";
    graph2.hideBulletsCount = 50; // this makes the chart to hide bullets when there are more than 50 series in selection
    chart.addGraph(graph2);

    // GRAPH
    var graph3 = new AmCharts.AmGraph();
    graph3.title = "sad %";
    graph3.valueField = "sad";
    graph3.bullet = "round";
    graph3.bulletBorderColor = "#FFFFFF";
    graph3.bulletBorderThickness = 2;
    graph3.lineThickness = 2;
    graph3.lineColor = "#0000ff";
    graph3.negativeLineColor = "#efcc26";
    graph3.hideBulletsCount = 50; // this makes the chart to hide bullets when there are more than 50 series in selection
    chart.addGraph(graph3);

    // CURSOR
    chartCursor = new AmCharts.ChartCursor();
    chartCursor.cursorPosition = "mouse";
    chartCursor.pan = true; // set it to fals if you want the cursor to work in "select" mode
    chart.addChartCursor(chartCursor);

    // SCROLLBAR
    var chartScrollbar = new AmCharts.ChartScrollbar();
    chart.addChartScrollbar(chartScrollbar);

    // LEGEND
    var legend = new AmCharts.AmLegend();
    chart.addLegend(legend);

    // WRITE
    chart.write("chartdiv");
});



// this method is called when chart is inited as we listen for "dataUpdated" event
function zoomChart() {
    // different zoom methods can be used - zoomToIndexes, zoomToDates, zoomToCategoryValues
    chart.zoomToIndexes(chartData.length - 40, chartData.length - 1);
}

