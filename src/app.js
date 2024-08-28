document.querySelector(".calculate-button").addEventListener("click", () => {
	// Get the type of it
	const lotType = document.querySelector("#park").value;
	console.log(lotType);

	// Get and Calculate Date
	const entryDate = new Date(
		document.querySelectorAll("input[type='date']")[0].value +
			"T" +
			document.querySelectorAll("input[type='time']")[0].value
	);
	const exitDate = new Date(
		document.querySelectorAll("input[type='date']")[1].value +
			"T" +
			document.querySelectorAll("input[type='time']")[1].value
	);

	// Check if exit date is before entry date
	if (exitDate < entryDate) {
		document.querySelector(".TotalCost").textContent =
			"Leaving date and time cannot be before Entry Date and Time";
		return;
	}

	const totalHours = (exitDate - entryDate) / (1000 * 60 * 60);
	let totalCost = 0;

	// calculate cost based on type
	switch (lotType) {
		case "Lot Parking":
			totalCost = Math.min(9, totalHours * 2);
			totalCost = Math.min(totalCost, 54);
			break;
		case "Hourly Parking":
			totalCost = 2 + Math.max(0, Math.ceil((totalHours - 1) * 2)) * 1;
			totalCost = Math.min(totalCost, 24);
			break;
		case "Garage Parking":
			totalCost = Math.min(12, totalHours * 2);
			totalCost = Math.min(totalCost, 72);
			break;
		case "Surface Parking":
			totalCost = Math.min(10, totalHours * 2);
			totalCost = Math.min(totalCost, 60);
			break;
		case "Valet Parking":
			if (totalHours <= 5) {
				totalCost = 12; // Valet Parking cost for 5 hours or less
			} else {
				totalCost = totalDays * 18; // Valet Parking daily rate
			}
		default:
			break;
	}

	document.querySelector(".TotalCost").textContent = `$${totalCost.toFixed(2)}`;
});
