(function () {
    var drawChart = function (canvasId, intervals, intervalType, datasetLocation) {
        var canvas = document.getElementById(canvasId);
        var context = canvas.getContext('2d');

        var chartOptions = {
            type: 'line',
            data: {
                labels: Array.apply(null, Array(intervals.length)).map((v, index) => {
                    let date = new Date();
                    const intervalIndex =  date["get" + intervalType]();

                    let pointer = index + intervalIndex;

                    if (intervalType === 'Month') {
                        pointer += 1;
                    }

                    if (pointer >= intervals.length) {
                        pointer -= intervals.length;
                    }

                    return intervals[pointer];
                }),
                datasets: [{
                    label: 'B',
                    borderColor: '#FF9BCA',
                    backgroundColor: '#FF9BCA',
                    fill: false,
                    data: chart_data[datasetLocation].bugs,
                }, {
                    label: 'F',
                    borderColor: '#C8FFDA',
                    backgroundColor: '#C8FFDA',
                    fill: false,
                    data: chart_data[datasetLocation].features,
                }]
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Breakdown of Bug and Feature Work'
                },
                tooltips: {
                    mode: 'index',
                    intersect: false,
                },
                hover: {
                    mode: 'nearest',
                    intersect: true
                },
                scales: {
                    xAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: intervalType + 's'
                        }
                    }],
                    yAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: 'Tickets worked on'
                        }
                    }]
                }
            }
        };

        new Chart(context, chartOptions);
    };

    document.addEventListener('DOMContentLoaded', function () {
        drawChart(
            'monthly-chart',
            ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            'Month',
            'monthly',
        );

        drawChart(
            'daily-chart',
            ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            'Day',
            'daily',
        );
    });
})();
