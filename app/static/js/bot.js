

//for getting querystring variable
function gup(name) {
  name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
  var regexS = "[\\?&]" + name + "=([^&#]*)";
  var regex = new RegExp(regexS);
  var results = regex.exec(window.location.href);
  if (results == null)
    return "";
  else
    return unescape(results[1]);
}

//http://127.0.0.1:5000/bot?context=stress&q=1&c=1&d=2


//elements
var sendBtn = document.getElementById('sendBtn');
var textbox = document.getElementById('textbox');
var chatContainer = document.getElementById('chatContainer');


var user = {message:"",counter:0};



var stress_hq_hc = [

     {"question":"Hello, I am Ustadbot, your life coach. I will listen to everything you have to say and help you guide yourself better. Tell me what brought you here today?", "answer":""},
     {"question":"That must have been very difficult for you. You are frustrated about not being able to have better balance work-home life despite doing your best. What difficulties have you had in relation to your problem?", "answer":""},
     {"question":"Thank you for sharing your struggles with me. I somehow sense that you feel guily of not being a good mom and you are also worried about your relationahip with your employer. What have you done to cope with these feelings?", "answer":""},
     {"question":"It seems like you are a really spirited and strong-willed person in a way. On one hand, you feel you have done all you could do to balance your work-home life, but on the other hand, you want to figure out what else you need to do. What concerns you the most?", "answer":""},
     {"question":"That’s a pretty common concern! I appreciate your willingness to discuss possible options. What supports do you draw on in your family, friends, or colleagues?", "answer":""},
     {"question":"Great! I will be happy give you some ideas, but I don’t want to get in the way of your own creative thinking, and you are the expert on you. Oops, but the time's almost up.  How do you feel after talking about it now?","answer":""}
];

var stress_lq_hc = [

     {"question":"Hello, I am Ustadbot. What is it you'd like to talk about?", "answer":""},
     {"question":"That's okay, we can talk about it. By the way what kind of job is it?", "answer":""},
     {"question":"It sounds good! Do you have partner in life that can support you?", "answer":""},
     {"question":"That seems reasonable! Do you think your employer will fire you if you go over your allotted amount of days?", "answer":""},
     {"question":"That seems good! Do you have any hobbies that allow you to relax in this situation?", "answer":""},
     {"question":"Fine! Do all those activities which gives you the most joy in your life and you will feel better :). Oops, but the time's almost up. How do you feel after talking about it now?","answer":""}
];

var stress_hq_lc = [

     {"question":"Hello, I am Ustadbot, your life coach. I will listen to everything you have to say and help you guide yourself better. Tell me what brought you here today?", "answer":""},
     {"question":"I have heard a lot of students say that! I understand that you have some concerns about your school perfromance. Can you tell me more about them?", "answer":""},
     {"question":"Anyone would feel this way if they were in your situation. You're feeling overwhelmed even with things that you used to be able to manage in the past. What do you imagine are the worst things that might happen to you?", "answer":""},
     {"question":"That’s a pretty common reaction! I can feel you. I have seen a lot of overly stressed students like you due to similar problems. What do you say to yourself that helps you cope?", "answer":""},
     {"question":"That's a good solution! They say life is trying things to see if they work. So let's not give up all the good things that you're are trying to cope! Oops, but the time's almost up! How do you feel after talking about it now?", "answer":""},
];

var stress_lq_lc = [

     {"question":"Hello, I am Ustadbot. What is it you'd like to talk about?", "answer":""},
     {"question":"That's sucks! What subjects you're studying?", "answer":""},
     {"question":"Interesting! May I ask what kind of grades you've been getting lately?", "answer":""},
     {"question":"That seems good! Have you been getting any feedback from professors?", "answer":""},
     {"question":"Fantastic! Maybe when you get stressed you stop for a minute and take a walk to relax or watch something interesting on Youtube. Oops, but the time's almost up! How do you feel after talking about it now?","answer":""}
];


var IR_hq_hc_health = [
     {"question":"Hi There! I am Talashbot, your search assistant. I am so glad you stopped by. Chances are you're looking for somehting in particular. What can I help you with today?", "answer":""},
     {"question":"Yes, it would be my pleasure to help! I have found two programs for your granny based on recommendations of American College of Sports Medicine (ACSM) and American Heart Association (AHA). First one is the Balance exercises that help prevent falls, a common problem in older adults. Tai chi is one example of balance exercises. Another one is the cardiorespiratory endurance which involves performing moderate-intensity aerobic activity at least 30 minutes on 5 days per week, such as brisk walking or jogging, dancing, climbing stairs or hills.", "answer":""}
];


var IR_hq_hc_science = [
     {"question":"Hi There! I am Talashbot, your search assistant. I am so glad you stopped by. Chances are you're looking for somehting in particular. What can I help you with today?", "answer":""},
     {"question":"Relax! It seems difficult but it is not. Building a derby car starts with these easily available materials including: Graphite, Derby kit, paint, painter’s tape, sandpaper, and a screw-on Zinc weight. Start with cutting and draw the car shape into a block and then do the side profiles and other body detailing. After that, you need to attach the weight for which you have to drill the location and fasten the weight there. Then you need to go for the last task, attaching wheels. Hammer the wheels on both sides and tight them.", "answer":""}
];

var IR_hq_hc_entertainment = [
     {"question":"Hi There! I am Talashbot, your search assistant. I am so glad you stopped by. Chances are you're looking for somehting in particular. What can I help you with today?", "answer":""},
     {"question":"Since the fictional character should be based on something that most of the people know, all around the world. What do you think about the Pandas? They are famous all over the world.  As Pandas have been noticed playing with balls too (there are several videos on the internet). And it also stands a perfect fit for small fun-actions performed with baseball-balls on the stadium. Furthermore, you need to choose from bright range of colors. It can be a bright yellow, orange, blue or purple.", "answer":""}
];


var IR_lq_hc_health = [
     {"question":"Hi There! I am Talashbot, your search assistant. What can I help you with today?", "answer":""},
     {"question":"Your granny can do swimming, walking, Yoga, different kinds of sitting and strengthening excercises. Here is the link for more details: https://www.asccare.com/best-low-impact-exercises-seniors/", "answer":""}
];


var IR_lq_hc_science = [
     {"question":"Hi There! I am Talashbot, your search assistant. What can I help you with today?", "answer":""},
     {"question":"Here are the steps, design your car on a paper, get your supplies, cut the wood, sand your car and paint it and put on the wheels. That’s it!", "answer":""}
];

var IR_lq_hc_entertainment = [
     {"question":"Hi There! I am Talashbot, your search assistant. What can I help you with today?", "answer":""},
     {"question":"What do you think about Penguins? They are damn so cute!.", "answer":""}
];



var IR_hq_lc_health = [
     {"question":"Hi There! I am Talashbot, your search assistant. I am so glad you stopped by. Chances are you're looking for somehting in particular. What can I help you with today?", "answer":""},
     {"question":"Thank you for asking. Approximately 1.2 million people in the U.S. are living with HIV today. About 14 percent of them (1 in 7) don’t know it and need testing.", "answer":""}
];


var IR_hq_lc_science = [
     {"question":"Hi There! I am Talashbot, your search assistant. I am so glad you stopped by. Chances are you're looking for somehting in particular. What can I help you with today?", "answer":""},
     {"question":"The deepest part of the ocean is called the 'Challenger Deep' and is located beneath the western Pacific Ocean in the southern end of the Mariana Trench, which runs several hundred kilometers southwest of the U.S. territorial island of Guam. Challenger Deep is approximately 36,200 feet deep.", "answer":""}
];

var IR_hq_lc_entertainment = [
     {"question":"Hi There! I am Talashbot, your search assistant. I am so glad you stopped by. Chances are you're looking for somehting in particular. What can I help you with today?", "answer":""},
     {"question":"In 2020, they'll solidify this second era of the band with their fifth full-length 'Thin Mind' out January 24th via Sub Pop. I have also found their official website where you can find more information: https://wolfparade.bandcamp.com/album/thin-mind", "answer":""}
];

var IR_lq_lc_health = [
     {"question":"Hi There! I am Talashbot, your search assistant. What can I help you with today?", "answer":""},
     {"question":"I think they are slightly over 1 million.", "answer":""}
];


var IR_lq_lc_science = [
     {"question":"Hi There! I am Talashbot, your search assistant. What can I help you with today?", "answer":""},
     {"question":"Challenger Deep", "answer":""}
];

var IR_lq_lc_entertainment = [
     {"question":"Hi There! I am Talashbot, your search assistant. What can I help you with today?", "answer":""},
     {"question":"Thin Mind!", "answer":""}
];



//here I will get all querystring data
//http://127.0.0.1:5000/bot?context=stress&q=1&c=1&d=2&cat=h
var botname = "";
var questionsToAsk = [];
// Stress task: high quality, high complexity
if(gup("context") == "stress" && gup("q") == "1" && gup("c") == "1") questionsToAsk=stress_hq_hc;
// Stress task: low quality, high complexity
if(gup("context") == "stress" && gup("q") == "0" && gup("c") == "1") questionsToAsk=stress_lq_hc;
// Stress task: high quality, low complexity
if(gup("context") == "stress" && gup("q") == "1" && gup("c") == "0") questionsToAsk=stress_hq_lc;
// Stress task: low quality, low complexity
if(gup("context") == "stress" && gup("q") == "0" && gup("c") == "0") questionsToAsk=stress_lq_lc;


// IR task: high quality, high complexity
if(gup("context") == "IR" && gup("q") == "1" && gup("c") == "1" && gup("cat") == "h") questionsToAsk=IR_hq_hc_health;
// IR task: low quality, high complexity
if(gup("context") == "IR" && gup("q") == "0" && gup("c") == "1" && gup("cat") == "h") questionsToAsk=IR_lq_hc_health;
// IR task: high quality, high complexity
if(gup("context") == "IR" && gup("q") == "1" && gup("c") == "1" && gup("cat") == "s") questionsToAsk=IR_hq_hc_science;
// IR task: low quality, high complexity
if(gup("context") == "IR" && gup("q") == "0" && gup("c") == "1" && gup("cat") == "s") questionsToAsk=IR_lq_hc_science;
// IR task: high quality, high complexity
if(gup("context") == "IR" && gup("q") == "1" && gup("c") == "1" && gup("cat") == "e") questionsToAsk=IR_hq_hc_entertainment;
// IR task: low quality, high complexity
if(gup("context") == "IR" && gup("q") == "0" && gup("c") == "1" && gup("cat") == "e") questionsToAsk=IR_lq_hc_entertainment;


// IR task: high quality, high complexity
if(gup("context") == "IR" && gup("q") == "1" && gup("c") == "0" && gup("cat") == "h") questionsToAsk=IR_hq_lc_health;
// IR task: low quality, high complexity
if(gup("context") == "IR" && gup("q") == "0" && gup("c") == "0" && gup("cat") == "h") questionsToAsk=IR_lq_lc_health;
// IR task: high quality, high complexity
if(gup("context") == "IR" && gup("q") == "1" && gup("c") == "0" && gup("cat") == "s") questionsToAsk=IR_hq_lc_science;
// IR task: low quality, high complexity
if(gup("context") == "IR" && gup("q") == "0" && gup("c") == "0" && gup("cat") == "s") questionsToAsk=IR_lq_lc_science;
// IR task: high quality, high complexity
if(gup("context") == "IR" && gup("q") == "1" && gup("c") == "0" && gup("cat") == "e") questionsToAsk=IR_hq_lc_entertainment;
// IR task: low quality, high complexity
if(gup("context") == "IR" && gup("q") == "0" && gup("c") == "0" && gup("cat") == "e") questionsToAsk=IR_lq_lc_entertainment;

if (gup("context") == "stress") botname = "UstadBot";
if (gup("context") == "IR") botname = "TalashBot";

function chatbotSendMessage(messageText){

    $('#messages_table tr:last').after("<tr><td><div style='float:left' class='profile-image'><img height='100%' src='/static/img/bot.png'></div><div class='left-arrow'></div><div class='bubble'><span style='font-size:10px;color:#999999;'>"+botname+" 11:40</span><br>"+messageText+"</div></td></tr>");

     //scroll to last message
     chatContainer.scrollTop = chatContainer.scrollHeight;

}


function sendMessage(messageText){
     $('#messages_table tr:last').after("<tr><td><div style='float:right' class='profile-image'><img height='100%' src='/static/img/person.png'></div><div class='right-arrow'></div><div class='bubble-me'><span style='font-size:10px;color:#d9d9d9;'>You  11:40</span><br>"+messageText+"</div></td></tr>");

     //scroll to last message
      chatContainer.scrollTop = chatContainer.scrollHeight;


}


// chat asks questions
function askQuestion(){
   if(user.counter == 0) delay = 0;
   else delay = parseInt(gup("d")) * 1000;

     if(questionsToAsk.length > user.counter){
          setTimeout(function(){

               chatbotSendMessage(questionsToAsk[user.counter].question);
               user.counter++;
          },delay);

     }



     // if((questionsToAsk.length - 1) == user.counter && gup("context") == "stress") {
     //   //add buttons
     // }

     console.log("q_len: "+questionsToAsk.length);
     console.log("counter: "+user.counter);
     console.log(questionsToAsk[user.counter-1]);

}



sendBtn.addEventListener('click', function(e){
    if(textbox.value.trim() == ""){
      e.preventDefault();
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
          if(textbox.value.trim() == ""){
               e.preventDefault();

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
