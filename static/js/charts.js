(function () {
    document.addEventListener('DOMContentLoaded', function () {
        console.log('rendering charts');

        var canvass = document.getElementById('breakdown-chart');
        var context = canvass.getContext('2d');

        var datasets = chart_data.map(data => ({
            label: data.label,
            data: [data.bugs, data.features],
            backgroundColor: ["#000000", "#FFFFFF"],
        }));

        console.log(datasets);

        var chartOptions = {
            type: 'bar',
            data: {
                labels: ["Bugs", "Features"],
                datasets,
            },
            options: {"scales": {"yAxes": [{"ticks": {"beginAtZero": true}}]}},
        };
        console.log(chartOptions);
        new Chart(context, chartOptions);

    });
})();
