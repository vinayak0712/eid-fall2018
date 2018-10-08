/**************************************************/
/*Author: Vinayak Srivatsan Kovalam Mohan *********/
/* HW 4:To write a Node.js program that reads 10
 values (one every 10 seconds) from the DHT22 
 sensor on my Pi and print out to the console
 log each reading as well as the lowest, highest
 and average of the readings 
 References: https://www.youtube.com/watch?v=mMAtxHPoodI
	     http://www.airspayce.com/mikem/bcm2835/
	     https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/min
	     https://www.w3schools.com/jsref/jsref_reduce.asp */

var sensorLib = require('node-dht-sensor');
var count = 0
var temp_array = []
var hum_array = []

var sensor = {
	sensors: [ {
		name: "Temperature",
		type: 22,
		pin: 4
	} ],
        read: function(){
        	for (var item in this.sensors){
			var list = sensorLib.read(this.sensors[item].type, this.sensors[item].pin);
			var hum = list.humidity;
			var celsius = list.temperature.toFixed(1);
			var fahreinheit = celsius * 1.8 + 32
			/* counter to count until 10 */
			count = count + 1
			/* array to store the obtained values */
			temp_array.push(fahreinheit)
			hum_array.push(hum)
			/* to print the count */
			console.log(count)
			console.log(this.sensors[item].name + ":" + fahreinheit + " degF    " + hum + "% Humidity");
			function getSum(total, num) {
    			return total + num;
			}
			if (count == 10){
				console.log("Lowest Temperature: " + Math.min(...temp_array) + " degF")
				console.log("Highest Temperatue: " + Math.max(...temp_array) + " degF")
				console.log("Lowest Humidity: " + Math.min(...hum_array) + " %")
				console.log("Highest Humidity: " + Math.max(...hum_array) + " %")			
				console.log("Average Temperature: " + temp_array.reduce(getSum)/ temp_array.length + " degF")
				console.log("Average Humidity: " + hum_array.reduce(getSum)/ hum_array.length + " %")
				process.exit(0)
			}		
}
		

		setTimeout(function() {
			sensor.read();
		}, 10000);
}	
 };

sensor.read();