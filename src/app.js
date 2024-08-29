document.querySelector(".calculate-button").addEventListener("click", () => {
	// Get the type of it
	const lotType = document.querySelector("#park").value;

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

	// Check if exit date is before entry date
	console.log(entryDate);
	console.log(exitDate);
	if (exitDate - entryDate == 0) {
		document.querySelector(".TotalCost").textContent = "$0";
		return;
	}

	let totalMinutes = Math.ceil((exitDate - entryDate) / (1000 * 60));
	let totalHours = totalMinutes / 60;
	const totalDays = Math.ceil(totalHours / 24);
	let totalCost = 0;

	// calculate cost based on type
	switch (lotType) {
		case "Lot Parking":
			if (totalHours <= 1) {
				totalCost = 2; // Minimum charge for up to one hour
			} else {
				totalCost = Math.min(9, totalHours * 2);
				if (totalCost == 9 && totalHours > 5) {
					totalCost = 54;
				}
			}
			break;
		case "Hourly Parking":
			if (totalMinutes <= 60) {
				totalCost = 2; // First hour charge
			} else {
				let additionalHalfHours = Math.ceil((totalMinutes - 60) / 30);
				totalCost = 2 + additionalHalfHours * 1; // First hour + additional half hours
			}
			totalCost = Math.min(totalCost, 24); // Daily maximum
			break;
		case "Garage Parking":
			if (totalHours <= 1) {
				totalCost = 2; // Minimum charge for up to one hour
			} else {
				totalCost = Math.min(12, totalHours * 2);
				if (totalCost == 12 && totalHours > 6) {
					totalCost = 72;
				}
			}
			break;
		case "Surface Parking":
			if (totalHours <= 1) {
				totalCost = 2; // Minimum charge for up to one hour
			} else {
				totalCost = Math.min(10, totalHours * 2);
				if (totalCost == 10 && totalHours > 5) {
					totalCost = 60;
				}
			}
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
