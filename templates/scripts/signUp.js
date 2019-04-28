$("#submit").click(function() {
	var email = $("#email").val();
	var password =  $("#password").val();
	signUp(email, password);
	
	setTimeout(function(){
		$("#post").click();
	}, 750);
	
});