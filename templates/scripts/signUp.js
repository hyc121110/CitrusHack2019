$("#submit").click(function() {
	var email = $("#email").val();
	var password =  $("#password").val();
	signUp(email, password);
	/*
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
	*/
	
	setTimeout(function(){
		$("#post").click();
	}, 1500);
	
});