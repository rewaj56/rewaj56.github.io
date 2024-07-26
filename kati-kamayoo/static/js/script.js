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
                    beginAtZero: true
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
                        text: 'Total Items Sold'
                    }
                },
                y2: {
                    type: 'linear',
                    position: 'right',
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Total Earnings'
                    },
                    grid: {
                        drawOnChartArea: false
                    }
                }
            }
        }
    });
});