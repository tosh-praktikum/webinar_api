let send_message = () => {
	// TODO: Errors

	let textarea = document.querySelector("#js-user-text")
	if (!textarea.value) {
		console.log("Message is empty")
		return
	}

	fetch('http://localhost:8000/send', {
		method: 'POST',
		body: JSON.stringify({"message": textarea.value})
	})
	.then(response => response.json())
	.then(json => {
		if (json.status === "ok") {
			console.log("Message has been sent")
			textarea.value = ""
		}
	})
	.catch(
		(error) => { console.error('Error:', error) }
	)
}