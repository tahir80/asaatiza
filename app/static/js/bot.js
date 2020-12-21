

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
var searchInput = "";
var category = "";
var isSearchTask = false;

var simple_health = "I recently watched a documentary about people living with HIV in the United States. I thought the disease was nearly eradicated, and am now curious to know more about the prevalence of the disease. Specifically, how many people in the US are currently living with HIV?";
var simple_science = "I recently watched a show on the Discovery Channel, about fish that can live so deep in the ocean that they're in darkness most or all of the time. This made me more curious about the deepest point in the ocean. What is the name of the deepest point in the ocean?";
var simple_entertainment = "I recently attended an outdoor music festival and heard a band called Wolf Parade. I really enjoyed the band and want to purchase their latest album. What is the name of their latest (full-length) album?";

var complex_health = "My great granny's doctor has told her that getting more exercise will increase her fitness and help her avoid injuries. I need an exercise program for her. She is 90-years old. Help me to put together two thirty-minute low impact exercise programs that she could alternate between during the week.";
var complex_science = "After the NASCAR season opened this year, my niece became really interested in soapbox derby racing. Since her parents are both really busy, I agreed to help her build a car so that she can enter a local race. The first step is to figure out how to build a car. Identify some basic designs that you might use and help me to create a basic plan for constructing the car.";
var complex_entertainment = "My local Triple-A affiliate baseball team has decided that it is time for a new mascot and are holding a contest where fans can enter suggestions. Being a loyal fan, I have decided to enter the contest. I want to suggest a mascot that will appeal to many people and will represent important qualities of a baseball team. The team is a part of the International League, so I want to avoid suggesting a mascot that is already represented in this league. Which mascot would I pick and why?";

var stress_hq_hc = [

     {"question":"Hello, I am Ustad, your life coach. I will listen to everything you have to say and help you guide yourself better. Tell me what brought you here today?", "answer":""},
     {"question":"That must have been very difficult for you. You appear to be frustrated about not being able to have a better work-life balance despite doing your best. What difficulties have you had in relation to your problem?", "answer":""},
     {"question":"Thank you for sharing your struggles with me. I sense that you feel guily of not being a good mom and you are also worried about your relationahip with your employer. What have you done to cope with these feelings?", "answer":""},
     {"question":"It seems like you are a really spirited and strong-willed person in a way. On one hand, you feel like you have done everything you could do to balance work and life, but on the other hand, you want to figure out what else you need to do. What concerns you the most?", "answer":""},
     {"question":"That's a fairly common concern! I appreciate your willingness to discuss possible options. What supports do you draw on in your family, friends, or colleagues?", "answer":""},
     {"question":"Great! They say life is about trying things to see if they work. So let's not give up on all the good things that you're are trying to help cope with this situation! I think you have some positive aspects to act on. How do you feel after talking about it now?","answer":""}
];

var stress_lq_hc = [

     {"question":"Hello, I am Ustad, your life coach. I will listen to everything you have to say and help you guide yourself better. Tell me what brought you here today?", "answer":""},
     {"question":"That's okay, we can talk about it. By the way what kind of job is it?", "answer":""},
     {"question":"It sounds good! Do you have partner in life who can support you? What does your partner do?", "answer":""},
     {"question":"That seems reasonable! Do you think your employer will fire you if you go over your allotted amount of days?", "answer":""},
     {"question":"That seems good! What else?", "answer":""},
     {"question":"Fine! Do all those activities which gives you the most joy in your life and you will feel better. How do you feel after talking about it now?","answer":""}
];

var stress_hq_lc = [

     {"question":"Hello, I am Ustad, your life coach. I will listen to everything you have to say and help you guide yourself better. Tell me what brought you here today?", "answer":""},
     {"question":"I have heard a lot of students say that! I understand that you have some concerns about your school performance. Can you tell me more about that?", "answer":""},
     {"question":"Anyone would feel this way if they were in your situation. You're feeling overwhelmed even with things that you used to be able to manage in the past. What do you imagine are the worst things that might happen to you?", "answer":""},
     {"question":"That’s a pretty common reaction! I can feel you. I have seen a lot of overly stressed students like you due to similar problems. What do you say to yourself that helps you cope?", "answer":""},
     {"question":"That's a good solution! They say life is about trying things to see if they work. So let's not give up on all the good things that you're are trying to help cope with this situation! I think you have some positive aspects to act on. How do you feel after talking about it now?", "answer":""},
];

var stress_lq_lc = [

     {"question":"Hello, I am Ustad, your life coach. I will listen to everything you have to say and help you guide yourself better. Tell me what brought you here today?", "answer":""},
     {"question":"That really sucks! What subjects are you studying?", "answer":""},
     {"question":"Interesting! May I ask what kind of grades you've been getting lately?", "answer":""},
     {"question":"That seems good! Have you been getting any feedback from professors?", "answer":""},
     {"question":"Fantastic! Maybe when you get stressed you can watch something interesting on Youtube. How do you feel after talking about it now?","answer":""}
];

var GeneralIR = [
     {"question":"Hi There! I am Talash, your search assistant. I am so glad you stopped by. Chances are you're looking for something in particular. What can I help you with today?", "answer":""}
];


var IR_hq_hc_health = [
     {"question":"Hi There! I am Talash, your search assistant. I am so glad you stopped by. Chances are you're looking for somehting in particular. What can I help you with today?", "answer":""},
     {"question":"Yes, it would be my pleasure to help! I have found two programs for your granny based on recommendations of American College of Sports Medicine (ACSM) and American Heart Association (AHA). First one is the Balance exercises that help prevent falls, a common problem in older adults. Tai chi is one example of balance exercises. Another one is the cardiorespiratory endurance which involves performing moderate-intensity aerobic activity at least 30 minutes on 5 days per week, such as brisk walking or jogging, dancing, climbing stairs or hills.", "answer":""}
];


var IR_hq_hc_science = [
     {"question":"Hi There! I am Talash, your search assistant. I am so glad you stopped by. Chances are you're looking for somehting in particular. What can I help you with today?", "answer":""},
     {"question":"Relax! It seems difficult but it isn't. Building a derby car starts with these easily available materials including: Graphite, Derby kit, paint, painter’s tape, sandpaper and a screw-on Zinc weight. Start with cutting and draw the car shape into a block and then do the side profiles and other body detailing. After that, you need to attach the weight for which you have to drill the location and fasten the weight there.  Then you need to go for the last task; attaching wheels. Hammer the wheels on both sides and tight them. Now the last thing, you need to beat that friction right? As lubricants aren’t allowed. We can agree upon graphite. Use it everywhere, in the wheels, axles, axle slots. And there you go. Your derby car is ready!", "answer":""}
];

var IR_hq_hc_entertainment = [
     {"question":"Hi There! I am Talash, your search assistant. I am so glad you stopped by. Chances are you're looking for somehting in particular. What can I help you with today?", "answer":""},
     {"question":"Since the mascot should be based on something that most people around the world are familiar with, how about a Panda? Pandas are famous all over the world, several videos of pandas playing with balls have gone viral on the internet. They also exhibit some qualities that make them a perfect athlete, such as climbing, swimming and even walking! When they walk, they look like a gigantic and powerful creature. Their white coat with black markings is unique and resembles with the most common jersey color in the baseball team. So imagine a mascot where a giant panda is standing on his legs and swinging his bat with a helmet on his head.", "answer":""}
];


var IR_lq_hc_health = [
     {"question":"Hi There! I am Talash, your search assistant. What can I help you with today?", "answer":""},
     {"question":"I think your granny can do different kinds of strengthening excercises. ", "answer":""}
];


var IR_lq_hc_science = [
     {"question":"Hi There! I am Talash, your search assistant. What can I help you with today?", "answer":""},
     {"question":"I think you can design your car on a paper, get your supplies, cut the wood and paint it. finally put on the wheels. That’s it!", "answer":""}
];

var IR_lq_hc_entertainment = [
     {"question":"Hi There! I am Talash, your search assistant. What can I help you with today?", "answer":""},
     {"question":"What do you think about Penguins? They are so cute!", "answer":""}
];



var IR_hq_lc_health = [
     {"question":"Hi There! I am Talash, your search assistant. I am so glad you stopped by. Chances are you're looking for somehting in particular. What can I help you with today?", "answer":""},
     {"question":"Thank you for asking. Approximately 1.2 million people in the U.S. are living with HIV today. About 14 percent of them (1 in 7) don’t know it and need testing.", "answer":""}
];


var IR_hq_lc_science = [
     {"question":"Hi There! I am Talash, your search assistant. I am so glad you stopped by. Chances are you're looking for somehting in particular. What can I help you with today?", "answer":""},
     {"question":"The deepest part of the ocean is called the 'Challenger Deep' and is located beneath the western Pacific Ocean in the southern end of the Mariana Trench, which runs several hundred kilometers southwest of the U.S. territorial island of Guam. Challenger Deep is approximately 36,200 feet deep.", "answer":""}
];

var IR_hq_lc_entertainment = [
     {"question":"Hi There! I am Talash, your search assistant. I am so glad you stopped by. Chances are you're looking for somehting in particular. What can I help you with today?", "answer":""},
     {"question":"In 2020, they'll solidify this second era of the band with their fifth full-length 'Thin Mind' out January 24th via Sub Pop. I have also found their official website where you can find more information: https://wolfparade.bandcamp.com/album/thin-mind", "answer":""}
];

var IR_lq_lc_health = [
     {"question":"Hi There! I am Talash, your search assistant. I am so glad you stopped by. Chances are you're looking for something in particular. What can I help you with today?", "answer":""},
     {"question":"I think they are slightly over 1 million.", "answer":""}
];


var IR_lq_lc_science = [
     {"question":"Hi There! I am Talash, your search assistant. I am so glad you stopped by. Chances are you're looking for something in particular. What can I help you with today?", "answer":""},
     {"question":"If I am not wrong, its Challenger Deep", "answer":""}
];

var IR_lq_lc_entertainment = [
     {"question":"Hi There! I am Talash, your search assistant. I am so glad you stopped by. Chances are you're looking for something in particular. What can I help you with today?", "answer":""},
     {"question":"ummm... maybe 'Cry Cry Cry'. Or wait it could be 'Thin Mind'", "answer":""}
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


function checkCatgory(cat) {
  if (gup("context") == "IR" && gup("q") == "1" && gup("c") == "1" && cat == "Health") {questionsToAsk = IR_hq_hc_health; searchInput = complex_health;}
  // IR task: low quality, high complexity
  if (gup("context") == "IR" && gup("q") == "0" && gup("c") == "1" && cat == "Health") {questionsToAsk = IR_lq_hc_health; searchInput = complex_health;}
  // IR task: high quality, high complexity
  if (gup("context") == "IR" && gup("q") == "1" && gup("c") == "1" && cat== "Science & Technology") {questionsToAsk = IR_hq_hc_science; searchInput = complex_science;}
  // IR task: low quality, high complexity
  if (gup("context") == "IR" && gup("q") == "0" && gup("c") == "1" && cat== "Science & Technology") {questionsToAsk = IR_lq_hc_science; searchInput = complex_science;}
  // IR task: high quality, high complexity
  if (gup("context") == "IR" && gup("q") == "1" && gup("c") == "1" && cat== "Entertainment") {questionsToAsk = IR_hq_hc_entertainment; searchInput = complex_entertainment;}
  // IR task: low quality, high complexity
  if (gup("context") == "IR" && gup("q") == "0" && gup("c") == "1" && cat== "Entertainment") {questionsToAsk = IR_lq_hc_entertainment; searchInput = complex_entertainment;}


  // IR task: high quality, high complexity
  if (gup("context") == "IR" && gup("q") == "1" && gup("c") == "0" && cat== "Health") {questionsToAsk = IR_hq_lc_health; searchInput = simple_health;}
  // IR task: low quality, high complexity
  if (gup("context") == "IR" && gup("q") == "0" && gup("c") == "0" && cat== "Health") {questionsToAsk = IR_lq_lc_health; searchInput = simple_health;}
  // IR task: high quality, high complexity
  if (gup("context") == "IR" && gup("q") == "1" && gup("c") == "0" && cat== "Science & Technology") {questionsToAsk = IR_hq_lc_science; searchInput = simple_science;}
  // IR task: low quality, high complexity
  if (gup("context") == "IR" && gup("q") == "0" && gup("c") == "0" && cat== "Science & Technology") {questionsToAsk = IR_lq_lc_science; searchInput = simple_science;}
  // IR task: high quality, high complexity
  if (gup("context") == "IR" && gup("q") == "1" && gup("c") == "0" && cat== "Entertainment") {questionsToAsk = IR_hq_lc_entertainment; searchInput = simple_entertainment;}
  // IR task: low quality, high complexity
  if (gup("context") == "IR" && gup("q") == "0" && gup("c") == "0" && cat== "Entertainment") {questionsToAsk = IR_lq_lc_entertainment; searchInput = simple_entertainment;}

}

if (gup("context") == "stress") botname = "UstadBot";
if (gup("context") == "IR") {botname = "TalashBot"; questionsToAsk = IR_hq_hc_health;}

function chatbotSendMessage(messageText){

  $.ajax({
          type: "POST",
          url: "/setTime",
          data: JSON.stringify({
            "nothing": {}
          }),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function(data) {
          console.log(JSON.stringify(data));
          }
      });

    $('#chat-history tr:last').after("<tr><td><div style='float:left' class='profile-image'><img height='100%' src='/static/img/bot.png'></div><div class='left-arrow'></div><div class='bubble'><span style='font-size:10px;color:#999999;'>"+botname+" 11:40</span><br>"+messageText+"</div></td></tr>");


    if((questionsToAsk.length - 1) == user.counter && gup("context") == "stress") {
      $('#textbox').prop('disabled', true);
      $('#sendBtn').prop('disabled', true);
      options = ["I am feeling relieved", "I am feeling neutral", "I am still feeling distressed"];
      quickReplies(options);

    }

    if((questionsToAsk.length - 1) == user.counter && gup("context") == "IR") {
      $('#textbox').prop('disabled', true);
      $('#sendBtn').prop('disabled', true);
      options = ["OK Thank you!", "OK Perfect!"];
      quickReplies(options);

    }

    if(user.counter == 0 && gup("context") == "IR") {
      $('#textbox').prop('disabled', true);
      $('#sendBtn').prop('disabled', true);
      options = ["Science & Technology", "Health", "Entertainment"];
      searchTaskInput(options);
    }
     //scroll to last message
     chatContainer.scrollTop = chatContainer.scrollHeight;

}

function sendMessage(messageText){
     $('#chat-history tr:last').after("<tr><td><div style='float:right' class='profile-image'><img height='100%' src='/static/img/person.png'></div><div class='right-arrow'></div><div class='bubble-me'><span style='font-size:10px;color:#d9d9d9;'>You  11:40</span><br>"+messageText+"</div></td></tr>");

      if(isSearchTask) {
        $.ajax({
                type: "POST",
                url: "/bot",
                data: JSON.stringify({
                  message: category,
                  workerId: gup("workerId"),
                  task_id: gup("task_id")
                }),
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function(data) {
                console.log(JSON.stringify(data));
                }
            });
       isSearchTask = false;
      }
      else {
       $.ajax({
               type: "POST",
               url: "/bot",
               data: JSON.stringify({
                 message: messageText,
                 workerId: gup("workerId"),
                 task_id: gup("task_id")
               }),
               contentType: "application/json; charset=utf-8",
               dataType: "json",
               success: function(data) {
               console.log(JSON.stringify(data));
               }
           });
         }




     //scroll to last message
      chatContainer.scrollTop = chatContainer.scrollHeight;


}

function handleQuickReplies(elem) {
   var text = $(elem).text();
    $('#chat-history tr:last').remove();
    sendMessage(text);
    $('#textbox').prop('disabled', false);
    $('#sendBtn').prop('disabled', false);
    setTimeout(exit, 2000);
 }

function handleSearchTask(elem) {
  isSearchTask = true;
  var cat = $(elem).text();
  category = cat;
   checkCatgory(cat);
   $('#chat-history tr:last').remove();
   sendMessage(searchInput);
   $('#textbox').prop('disabled', false);
   $('#sendBtn').prop('disabled', false);
   // user.counter += 1;
   askQuestion();

}

function quickReplies(options) {
  var q = "<tr><td><div style='width:100%;text-align:center;'>";
  var arrayLength = options.length;
  for (var i = 0; i < arrayLength; i++) {
    q += "<div class='button' value='123' onclick='handleQuickReplies(this)'>" + options[i] + "</div>";
    console.log(options[i]);
  }

 q+= "</div></td></tr>";
 $('#chat-history tr:last').after(q);


 // handleQuickReplies(q);

 console.log(q);

}


function searchTaskInput() {
  var q = "<tr><td><div style='width:100%;text-align:center;'>";
  var arrayLength = options.length;
  for (var i = 0; i < arrayLength; i++) {
    q += "<div class='button' value='123' onclick='handleSearchTask(this)'>" + options[i] + "</div>";
    console.log(options[i]);
  }

 q+= "</div></td></tr>";
 $('#chat-history tr:last').after(q);

 // handleQuickReplies(q);

 console.log(q);
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

     //at the end of stress management task, ask user about their experience via buttons.


     console.log("q_len: "+questionsToAsk.length);
     console.log("counter: "+user.counter);
     console.log(questionsToAsk[user.counter-1]);

}

function exit() {
 document.getElementById('id01').style.display='block';

}

$("#next").click(function() {
  var qs = {
    'workerId': gup("workerId"),
    'task_id': gup("task_id"),
    'mood': gup("mood"),
    'context': gup("context"),
    'q': gup('q'),
    'c':gup('c'),
    'd':gup('d')
  };


window.location.replace("http://127.0.0.1:5000/exit_surveys" + "?" + $.param(qs));


});

// $(document).ready(function() {
// });



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
