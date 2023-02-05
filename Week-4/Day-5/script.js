var moneyInAcc = 1000;
var VAT = .17;
var PLMonth = 100;

function totalVAT (vat, PL){
    // If theres a loss then i dont have to pay vat so the total vat paid is 0
    if(PL <= 0){
        return 0;
    }else{
        //  If theres a profit then i have to pay vat on profits realized which is the percentage rate of vat multiplied by profits
        let total = vat*PL;
        return total;
    }
    
    
}
function updateAcc(vat, PL,moneyInAcc){
    if(totalVAT(vat,PL) == 0){
        let total = moneyInAcc + PL; //There was a loss so zero vat has to be paid - numbers are added to calculate a positive plus a negative number
        return total;
    } else{
        let total  = moneyInAcc + PL - totalVAT(vat, PL); //Money i started off with, i add my profit, then remove the calculated vat i must pay on those profits
        return total;
    }
}
console.log(updateAcc(VAT, PLMonth, moneyInAcc));

