function drawChart(id) {
  const ctx = document.getElementById(id);

  new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
          label: '# of Votes',
          data: [12, 19, 3, 5, 2, 3],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        },
      }
  });
}

drawChart('chart1');
drawChart('chart2');
drawChart('chart3');
drawChart('chart4');