

    window.onload = function(){

    var ctx = document.getElementById("chartHours").getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'line',
      data: {
	   labels: ['1999','2001','2003','2005','2007','2009', '2011', '2013', '2015', '2017', '2019', '2020'],

	  datasets: [{

		  data: [80.125, 21.625, 14.36, 76.9, 85.73, 90.13, 339.32, 455.49, 117.16, 143.66, 166.44,350.1],
		  backgroundColor :['rgba(149, 149, 149, 0.2)',
				'rgba(54, 162, 235, 0.2)',
				'rgba(255, 206, 86, 0.2)',
			  	'rgba(75, 192, 192, 0.2)',
				'rgba(153, 102, 255, 0.2)',
				'rgba(255, 159, 64, 0.2)'
          ],

          borderColor: [
				'rgba(99,255,222,,1)',
				'rgba(54, 162, 235, 1)',
				'rgba(255, 206, 86, 1)',
				'rgba(75, 192, 192, 1)',
				'rgba(153, 102, 255, 1)',
				'rgba(255, 159, 64, 1)'
			],
borderWidth : 1
	}
	]
},
options: {

        responsive:true,
         tooltips:{mode:'index', intersect: false},
<!--&lt;!&ndash;        hover:{mode:'label'},&ndash;&gt;-->

<!--events: ['mousemove'],-->
       hover: {
          mode:'nearest',
          intersect:true,
        },
		scales: {
			yAxes: [{
				ticks: {
					beginAtZero:true,
				  max:700  ,
					maxTicksLimit:10
				},

				scaleLabel: {
                    display: true,
                    labelString: 'Stock Price',
                    fontSize:20,
                  },

<!--				gridLines:{-->

<!--				    drawBorder:true,-->
<!--				    display:false-->
<!--				}-->
			}],

			xAxes:[{
                    scaleLabel: {
                    display: true,
                    labelString: 'Year',
                    fontSize:20
                  },
<!--			      gridLines:{-->

<!--				    drawBorder:true,-->
<!--				    display:false-->
<!--				}-->
			}]
		},

<!--		maintainAspectRatio: false,-->
		legend:{display: false},
		elements:{
		    point:{
		      radius:0
		    }
		},
	}
});
}
