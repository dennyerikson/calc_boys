
$(document).ready(function() {
  var url = "/score_json/";

  $.getJSON(url, function(res){
    var data = res.aluno.map(function(v){
      return [v.data, v.quantidade]
    })  

    var data2 = res.aluno.map(function(v){
      return [v.data, v.acertos]
    }) 

    var dataerros = res.aluno.map(function(v){
      return [v.data, v.erros]
    }) 
    

    Highcharts.setOptions({
      lang: {
        drillUpText: '<< Voltar '
      }
    });
  
    Highcharts.chart('container_pontos', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Pontos'
      },
      subtitle: {
        text: 'Quantidade de pontos nos treinamentos'
      },
      xAxis: {
        type: 'category'
      },
      yAxis: {
        title: {
          text: 'Pontos'
        }
      },
      legend: {
        enabled: false
      },
      plotOptions: {
        series: {
          borderWidth: 1,
          dataLabels: {
            enabled: true,
            format: '{point.y}'
          }
        }
      },

      tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y}</b> do total<br/>'
        // pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> do total<br/>'
      },    
  
      series: [
        {
        name: 'Pontos',
        colorByPoint: true,

        data: data

      },
      // {
      //   name: 'Acertos',
      //   colorByPoint: true,

      //   data: data2

      // }
    ],
    });



    Highcharts.chart('container_line', {

      title: {
          text: 'Acertos e Erros'
      },
  
      subtitle: {
          text: 'Quantidade de pontos nos treinamentos'
      },
  
      yAxis: {
          title: {
              text: 'Numeros de Acertos e Erros'
          }
      },
      legend: {
          layout: 'vertical',
          align: 'right',
          verticalAlign: 'middle'
      },
  
      plotOptions: {
          series: {
              label: {
                  connectorAllowed: false
              },
              pointStart: data['v.data']
          }
      },
  
      series: [
        {
          name: 'Acertos',
          data: data2
    
        },
        {
          name: 'erros',
          data: dataerros
    
        },
      ],
  
      responsive: {
          rules: [{
              condition: {
                  maxWidth: 500
              },
              chartOptions: {
                  legend: {
                      layout: 'horizontal',
                      align: 'center',
                      verticalAlign: 'bottom'
                  }
              }
          }]
      }
  
  });
  });
// grafico do total de Candidatos 



  
});
  