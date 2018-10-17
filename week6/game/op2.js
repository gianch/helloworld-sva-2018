var ballX = 500; // initial x position
var ballY = 250; // initial y position

var ballXV = -9; //velocity
var ballYV = 1; // velocity

var player1X = 10;
var player1Y = 200;

var player2X = 970;
var player2Y = 200;

var p1 = 8;
var p2 = 8;

var intro = "Press Space Bar to Start Game";
var value = 0;

function setup() {
  createCanvas(1000, 500);
  background("#0D0D0D");
  noStroke();
}

function keyPressed() {

 // Space bar to start and pause the game

  if(keyCode == 32) {
    value += 1;
  }
}

function draw() {  
  fill(0, 255, 0); 
  rect(500,30,50,50);
  background("#0D0D0D");
  setShapes();
  setText();
  keyMove();   
  bounceCheck();
  scoreCheck();
  if (value % 2) {
    increment();
  }
}

function increment() {  
  ballX += ballXV;  
  ballY += ballYV;
  
  if(millis() % 1000 == 0) {
    ballXV = ballXV * 2;
  }
}

function keyMove() {

  // set W move up
  if (keyIsDown(87) && player1Y != 0){
    player1Y -= 10;
  }
    

   // set S move down
  if (keyIsDown(83) && player1Y != 400)
    player1Y += 10;

    // set UP arrow move up
  if (keyIsDown(UP_ARROW) && player2Y != 0)
    player2Y -= 10;

    // set DOWN arrow move up
  if (keyIsDown(DOWN_ARROW) && player2Y != 400)
    player2Y += 10;
}


function ball(x, y) {
  ellipse(x - 2, y, 20, 20);
  ellipse(x, y, 15, 15);
}

function setShapes() {
  fill(255);
  ball(ballX, ballY);
  fill(255);
  fill(255);
  fill("#07F8B6"); // green color
  rect(player1X, player1Y, 20, 100);
  fill("#F8DF4B"); // yellow color
  rect(player2X, player2Y, 20, 100);
}

function sliderBounce() {
  if(player1Y < ballY && player1Y + 100 > ballY) {
    ballXV = ballXV * -1;
  }
  if (player1Y + 50 == ballY) {
    ballXV = ballXV * -1;
  }
  if(player2Y < ballY && player2Y + 100 > ballY) {
    ballXV = ballXV * -1;
  }
  if (player2Y + 50 == ballY) {
    ballXV = ballXV * -1;
  }
  // sets limit for bar distance
  // if(player1Y < 0) {
  //   player1Y = 0;
  // }

  // if(player1Y > 500) {
  //   player1Y = 500;
  // }
  // if(player2Y < -500) {
  //   player2Y = -500;
  // }
  // if(player2Y > 500) {
  //   player2Y = 500;
  // }
}

function bounceCheck() {
  if(ballY < 0 || ballY > 500) {
    ballYV = ballYV * -1;
  }
  
  if(ballX < 40 && ballXV < 0) {
    sliderBounce();
  }
  
  if(ballX > 970 && ballXV > 0) {
    sliderBounce();
  }
  
  if(ballX < 0) {
    ballX = 500;
    p1 -= 1;
  }

  if(ballX > 1000) {
    ballX = 500;
    ballY = 250;
    p2 -= 1;
    value = 0;
  }
}

function scoreCheck() {
  if(p1 == 0) {
    //stop the ball
    ballXV = 0;
    ballYV = 0;
    result = "Player 2 Wins!";
    fill("#F8DF4B"); // yellow color
    setWinner();
    resetGame();
  }
  if(p2 == 0) {
    //stop the ball
    ballXV = 0;
    ballYV = 0;
    result = "Player 1 Wins!";
    fill("#07F8B6"); // green color
    setWinner();
    resetGame();
  }
}

function setText() {
  textAlign(CENTER);
  textSize(30);
  fill("#07F8B6"); // green color
  text(p1, 460, 50);
  fill("#F8DF4B"); // yellow color
  text(p2, 520, 50);
}

function setWinner() {
  textAlign(CENTER);
  textSize(30);
  text(result, 500, 100);
}

function resetGame() {

  if (keyCode == RETURN) {
    p1 = 8;
    p2 = 8;
    value = 0;
    ballXV = -9;
    ballYV = 1;
    if (value % 2) {
      increment();
    }
  }
}