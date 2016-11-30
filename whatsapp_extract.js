function getstuff(){
	var z =1;
	var x = document.getElementsByClassName("emojitext selectable-text");
		//var y = document.getElementByClassName("bubble bubble-text");

 	var data = x[x.length-1].innerText;
	if(data=="@Ging" && z){
		console.log(data);
		z=0;
	}
}

function replystuff(){
	var x = document.getElementByClassName("input-placeholder");

}


(function(document){
	setInterval(function(){
		getstuff()

		}, 8000);

})(document);



//false_919643343523@c.us_95B5DF8E51F46EDF16338D90751D37

//true_919643343523@c.us_6D9877CF69126DABE9AE99AF64C2B9

//false_919643343523@c.us_C7D4D7D4715B06B5066FD1020933FC