const ctx = document.getElementById('myffChart');

new Chart(ctx, {
  type: 'line',
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
	}
  }
});

var config = {
	type: 'line',
	data: {
	  datasets: [{
		data: [12, 19, 3, 5, 2, 3],
		backgroundColor: [
		  '#696969', '#808080', '#A9A9A9', '#C0C0C0', '#D3D3D3'
		],
		label:  ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
	  }],
	  
	},
	options: {
	  responsive: true
	}
  };

  window.onload = function() {
	var ctx = document.getElementById('myffchart').getContext('2d');
	window.myPie = new Chart(ctx, config);
  };