document.addEventListener('DOMContentLoaded', function() {
    const monthsBR = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'];
    //console.log(monthsBR); isso aqui eu volto depois pra ver
    const tableDays = document.getElementById('dias');
    function GetDaysCalendar(mes,ano){
        document.getElementById('mes').innerHTML = monthsBR[mes];
        //console.log(monthsBR[mes);
        document.getElementById('ano').innerHTML = ano;
        let firstDayOfWeek = new Date(ano,mes,1).getDay()-1;
        let getLastDayThisMonth = new Date(ano,mes+1,0).getDate();

        for(var i = -firstDayOfWeek, index = 0; i <(42 - firstDayOfWeek); i++,index++){
            let dt = new Date(ano,mes,i);
            let dayTable = tableDays.getElementsByTagName('td')[index];
            dayTable.innerHTML = dt.getDate();
            
            if(i < 1){
                dayTable.classList.add('mes-anterior')
            }
            if(i>getLastDayThisMonth){
                dayTable.classList.add('proximo-mes')
            }
        }
    }

    let now = new Date();
    let mes = now.getMonth();
    let ano = now.getFullYear();
    GetDaysCalendar(mes,ano);

    const botao_proximo = document.getElementById('btn_prev');
    const botao_anterior = document.getElementById('btn_next');

    botao_proximo.onclick = function(){
        if(mes == 0) {
            mes = 11;
            ano--;
        } else {
            mes--;
        }
        GetDaysCalendar(mes,ano);   
    }
    botao_anterior.onclick = function(){
        if (mes == 11) {
            mes = 0;
            ano++;
        } else {
            mes++;
        }
        GetDaysCalendar(mes,ano); 
    }

})