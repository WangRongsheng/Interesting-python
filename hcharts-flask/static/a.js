var chart = null; // 定义全局变量
var data = {};
$(document).ready(function () {
    $.get({
        url: '/get_data/',
        'success': function (point) {
            data = point;
        },
    });
    chart = chartfunc();
    chart.credits.update({
				text: 'Power by zhouluobo',
				href: 'https://www.luobodazahui.top/',
			});
    return data;
});

function chartfunc(){
    chart = Highcharts.chart('container', {
        chart: {
            type: 'spline',
        },
        title: {
            text: '新型冠状病毒肺炎走势'
        },
        xAxis: {
            type: 'category',
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: '确诊人数',
                margin: 80
            }
        },
        series: [{
            name: '每日新增',
            data: []
        },
            {
                name: '累计确诊',
                data: []
            }]
    });
    return chart;
}


/**
 * Ajax 请求数据接口，并通过 Highcharts 提供的函数进行动态更新
 * 接口调用完毕后间隔 1 s 继续调用本函数，以达到实时请求数据，实时更新的效果
 */

$('#button').click(function () {
    var req_data = data;
    //具体的参数详见：https://api.hcharts.cn/highcharts#Series.addPoint
    var index=0;
    var handler = setInterval(function () {
        funt();
    },500);
    function funt() {
        if(index<req_data['today'].length){
        index++;
        if(index>=req_data['today'].length){
            clearInterval(handler); //关闭定时
        }
        chart.series[0].addPoint(req_data['today'][index]);
        chart.series[1].addPoint(req_data['total'][index]);
    }
    }
});