$("#submit").click(function() {
	var email = $("#email").val();
	var password =  $("#password").val();
	login(email, password);
	admin.auth().getUser(uid)
  .then(function(userRecord) {
    // See the UserRecord reference doc for the contents of userRecord.
    console.log('Successfully fetched user data:', userRecord.toJSON());
  })
  .catch(function(error) {
    console.log('Error fetching user data:', error);
  });
});