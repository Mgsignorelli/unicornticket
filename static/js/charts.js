(function () {
    document.addEventListener('DOMContentLoaded', function () {
        var canvas = document.getElementById('breakdown-chart');
        var context = canvas.getContext('2d');
        var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        var chartOptions = {
            type: 'line',
            data: {
                labels: Array.apply(null, Array(12)).map((v, index) => {
                    let date = new Date();
                    const current_month = date.getMonth();
                    const month = current_month - (12 - index - 1);
                    date = date.setMonth(month);

                    return months[(new Date(date)).getMonth()];
                }),
                datasets: [{
                    label: 'B',
                    borderColor: '#FF9BCA',
                    backgroundColor: '#FF9BCA',
                    fill: false,
                    data: chart_data.bugs,
                }, {
                    label: 'F',
                    borderColor: '#C8FFDA',
                    backgroundColor: '#C8FFDA',
                    fill: false,
                    data: chart_data.features,
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
                            labelString: 'Month'
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
    });
})();