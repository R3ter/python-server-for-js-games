let force=0
let array=[]
let y=200;
const x=30
let xb=500
let time=5000
let score=0
let newblocks;
let lose=false;

document.onkeypress=(event)=>{move(event)}

var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
ctx.font = "30px Arial";

function render(timer){
   if(!lose){
      ctx.clearRect(0, 0, canvas.width, canvas.height);
   }else{
      ctx.clearRect(0, 0, 100, canvas.height);
   }

if(y<0){
y=0
}
if(y>690){
y=690
}
draw()

}

function draw(){
blocks()
ctx.beginPath();
ctx.fillStyle = "#000000";
ctx.rect(30, y, 30, 30);
ctx.fill();
ctx.closePath();
y=y-force
}

function gravity(){
   if(lose){
      force=0
      y=y+25
   }
   else{
      y=y+17
   }
}

function move(event){
if(event.keyCode==32){
up()
}
}
let jump
function up(){
   if(!lose){
      if(jump){
      //force=0
      clearInterval(jump)
      }
      let times=5;
      jump=setInterval(()=>{
      if(times>0){
      times=times-1
      force=force+10
      }else{
      clearInterval(jump)
      }
      },51)
   }
}


let timer=setInterval(()=>{render(timer)},51)

setInterval(gravity,51)
setInterval(()=>{
if(force>0){
force=force-10
}
},100)

function blocks(){
   for(let l=0; l<array.length; l++){
      if(!array[l].done){
         let height=array[l].height
         let xb=array[l].xb
         ctx.font = "30px Arial";
         ctx.beginPath();
         ctx.fillStyle = "#000000";
         ctx.fillText("score: "+score, 480, 50);
         ctx.rect(xb, 0, 30, height);
         ctx.rect(xb, 720, 30, height-720-200);
         ctx.fill();
         ctx.closePath();
         
   if(!lose){
      array[l].xb=array[l].xb-10  
      if(xb<0){
         array[l].done=true
         if(time>1000){
            time=time-100
         }
         score=score+1
         if(newblocks){
            clearInterval(newblocks)
            newblocks=setInterval(createnew,time)
         }
      }
      
      if (x < xb + 30 &&
         x + 30 > xb &&(
            y < 0 + height-200||y > height) &&
            y + 30 > 0)
            {
               console.log('loser')
               const gameover=setInterval(()=>{loserpanel(gameover)},51)
               lose=true
            }
         }
      }}
   }
const createnew=()=>{
array.push({height:(Math.floor(Math.random() * (620-200)))+200,
xb:1080
})
}

function loserpanel(){
   if(lose){
      ctx.beginPath();
      ctx.font = "60px Arial";
      ctx.fillStyle='#000000'
      ctx.fillText("Game Over", 440, 300);
      ctx.font = "30px Arial";
      ctx.fillStyle='#ff0000'
      ctx.fillText("click to restart", 480, 500);
      ctx.fill();
      ctx.closePath(); 
   }
       canvas.onclick=()=>{
          if(lose){
             score=0;
             time=5000
             array=[]
             y=200
             force=0
             lose=false;
          }
       }
}

newblocks=setInterval(createnew,time)