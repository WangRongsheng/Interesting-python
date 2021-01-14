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
            type: 'bar',
        },
        title: {
            text: '新型冠状病毒肺炎走势'
        },
        xAxis: {
            type: 'category',
            title: {
                text: '确诊人数'
            },
            labels: {
				enabled: false
			}
        },
        yAxis: {
            title: {
                text: null
            },
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                    // ,allowOverlap 默认是 false，即不允许数据标签重叠
                }
            }
        },
        series: [{
            name: '每日新增',
            data: [0],
            dataLabels: {
				format: '{point.y}'
			}
        },
            {
                name: '累计确诊',
                data: [0],
                dataLabels: {
				    format: '{point.y}'
			    }
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
    var index=0;
    var handler = setInterval(function () {
        funt();
    },500);
    function funt() {
        if(index<req_data['total'].length){
        if(index>=req_data['total'].length){
            clearInterval(handler); //关闭定时
        }
        chart.series[0].data[0].update({
            y: req_data['today'][index]['y']
        });
        chart.series[1].data[0].update({
            y: req_data['total'][index]['y']
        });
        index++;
    }
    }
});