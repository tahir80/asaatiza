
//Data Collection (asking questions)




//elements
var sendBtn = document.getElementById('sendBtn');
var textbox = document.getElementById('textbox');
var chatContainer = document.getElementById('chatContainer');


var user = {message:"",counter:0};



var questionsToAsk = [

     {"question":"Hello, I am Ustadbot, your life coach. I will listen to everything you have to say and help you guide yourself better. Tell me what brought you here today?", "answer":""},
     {"question":"how old are you?", "answer":""},
     {"question":"what's your job title?", "answer":""},
     {"question":"how old are you?", "answer":""},
     {"question":"where do you live?","answer":""}
];



function chatbotSendMessage(messageText){


    var messageElement = document.createElement('div');
    messageElement.classList.add('message_bubble');
    // messageElement.classList.add('float-left');
    // messageElement.classList.add('shadow-sm');
    // messageElement.style.margin ="10px";
    // messageElement.style.padding ="5px";

    // messageElement.innerHTML = "<span>Chatbot: </span>"+
    // "<span style="+"margin-top:10px; padding:10px"+">"+ messageText +"</span>";
    // console.log(messageText);

    messageElement.innerHTML = "<img src='bot.png' alt='Avatar' style='width:100%;'><p>"+messageText+"</p>";

    messageElement.animate([{easing:"ease-in",opacity:0.4},{opacity:1}],{duration:1000});
    chatContainer.appendChild(messageElement);

     //scroll to last message
     chatContainer.scrollTop = chatContainer.scrollHeight;

}



function sendMessage(messageText){

     var messageElement = document.createElement('div');
     messageElement.classList.add('message_bubble')
     messageElement.classList.add('darker');
     // messageElement.classList.add('float-right');
     // messageElement.classList.add('shadow-sm');
     // messageElement.style.margin ="10px";
     // messageElement.style.padding ="5px";

     // messageElement.innerHTML = "<span>You: </span>"+
     // "<span style="+"margin-top:10px; padding:10px"+">"+ messageText +"</span>";
     messageElement.innerHTML = "<img src='woman.png' alt='Avatar' style='width:100%;' class='right'><p>"+messageText+"</p>";

     messageElement.animate([{easing:"ease-in",opacity:0.4},{opacity:1}],{duration:1000});

     chatContainer.appendChild(messageElement);

     //scroll to last message
      chatContainer.scrollTop = chatContainer.scrollHeight;


}




// chat asks questions
function askQuestion(){


     if(questionsToAsk.length > user.counter){
          setTimeout(function(){

               chatbotSendMessage(questionsToAsk[user.counter].question);
               user.counter++;
          },1000);


     console.log(questionsToAsk[user.counter-1]);
     }

}









sendBtn.addEventListener('click', function(e){

    if(textbox.value == ""){
      e.preventDefault()
     // alert('Please type in a message');

    }else{

     let messageText = textbox.value.trim();
     user.message = messageText;
     sendMessage(messageText);
     textbox.value = "";

    //store user's answer to coresponding question
    questionsToAsk[user.counter-1].answer = user.message;


    //ask next question
     askQuestion();




    }
});



textbox.addEventListener('keypress',function(e){

     //if user hits the enter button on keyborad (13)
      if(e.which == 13){
          if(textbox.value == ""){
               alert('Please type in a message');

              }else{

               let messageText = textbox.value.trim();
               user.message = messageText;
               sendMessage(messageText);
               textbox.value = "";

               questionsToAsk[user.counter-1].answer = user.message;

                askQuestion();


              }


      }


});


askQuestion();
