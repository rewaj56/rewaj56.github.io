document.addEventListener('DOMContentLoaded', function() {
    var ctxEarnings = document.getElementById('earningsChart').getContext('2d');
    var ctxItemsSold = document.getElementById('itemsSoldChart').getContext('2d');
    
    new Chart(ctxEarnings, {
        type: 'bar',
        data: {
            labels: brandLabels,
            datasets: [{
                label: 'Total Earnings',
                data: earningsData,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: 'rgba(235, 234, 234, 1)'  // Change y-axis text color to white
                    }
                },
                x: {
                    ticks: {
                        color: 'rgba(235, 234, 234, 1)'  // Change x-axis text color to white
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        color: 'rgba(235, 234, 234, 1)'  // Change legend text color to white
                    }
                }
            }
        }
    });
    

    new Chart(ctxItemsSold, {
        type: 'line',
        data: {
            labels: brandLabels,
            datasets: [{
                label: 'Total Items Sold',
                data: itemsSoldData,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1,
                yAxisID: 'y1',
            }, {
                label: 'Total Earnings',
                data: earningsData,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1,
                yAxisID: 'y2',
            }]
        },
        options: {
            scales: {
                y1: {
                    type: 'linear',
                    position: 'left',
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Total Items Sold',
                        color: 'white'  // Set title text color to white
                    },
                    ticks: {
                        color: 'white'  // Set y1 axis ticks color to white
                    }
                },
                y2: {
                    type: 'linear',
                    position: 'right',
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Total Earnings',
                        color: 'white'  // Set title text color to white
                    },
                    grid: {
                        drawOnChartArea: false
                    },
                    ticks: {
                        color: 'white'  // Set y2 axis ticks color to white
                    }
                },
                x: {
                    ticks: {
                        color: 'white'  // Set x-axis labels color to white
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        color: 'white'  // Set legend text color to white
                    }
                }
            }
        }
    });    
});