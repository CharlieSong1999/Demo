/*
 *求由绿到红的渐变色值,百分比 bili 取值 1...100
 */
export function getColorByBaiFenBi(bili: number) {
  //var 百分之一 = (单色值范围) / 50;  单颜色的变化范围只在50%之内
  var one = (255 + 255) / 100;
  var r = 0;
  var g = 0;
  var b = 0;

  if (bili < 50) {
    // 比例小于50的时候红色是越来越多的,直到红色为255时(红+绿)变为黄色.
    r = one * bili;
    g = 255;
  }
  if (bili >= 50) {
    // 比例大于50的时候绿色是越来越少的,直到0 变为纯红
    g = 255 - (bili - 50) * one;
    r = 255;
  }
  r = parseInt(r + ""); // 取整
  g = parseInt(g + ""); // 取整
  b = parseInt(b + ""); // 取整

  //console.log("#"+r.toString(16,2)+g.toString(16,2)+b.toString(16,2));
  //return "#"+r.toString(16,2)+g.toString(16,2)+b.toString(16,2);
  //console.log("rgb("+r+","+g+","+b+")" );
  return "rgb(" + r + "," + g + "," + b + ")";
}

export function get_max(value: any) {
  return Math.ceil(value.max * 10) / 10;
}

export function get_min(value: any) {
  return Math.floor(value.min * 10) / 10;
}
