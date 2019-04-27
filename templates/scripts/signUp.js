$("#submit").click(function() {
	var email = $("#email").val();
	var password =  $("#password").val();
	
	var user = firebase.auth().currentUser;
	user.updateProfile({
	  displayName: "emp"
	}).then(function() {
		var displayName = user.displayName;
		console.log(displayName + " good.");
		$("#post").click();
	}).catch(function(error) {
		console.log("fail.");
	});
	
	
});