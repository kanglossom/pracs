const num = prompt("숫자를 입력하세요");
const str = String(num);
const arr = Array.from(str);

//숫자 입력받아서 배열로 끊는것까지 성공.

//예를 들어 110011을 입력받았다....
//맨 앞에 1에 2의 5승을 곱해야한다. 그다음 1은 2의 4승을 곱해야겠죠

var j = arr.length - 1; //110011일때 arr.length는 6. j=5
var i=0;
var k = 0;

while(j>=0){ //아니 j가 그럼 5에서 0까지 줄어들꺼아님.
    var num2 = Math.pow(2,j);
    var x = arr[i] * num2;
    k += x;
    i++;
    j--;
}
console.log(k);