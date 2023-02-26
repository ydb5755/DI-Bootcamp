function checkCashRegister(price, cash, cid) {
    let values = { 
      'ONE HUNDRED':100,
      'TWENTY':20,
      'TEN':10, 
      'FIVE':5, 
      'ONE':1,
      'QUARTER':0.25,
      'DIME':0.1, 
      'NICKEL':0.05, 
      'PENNY':0.01
    }
    let changeToGive = cash - price;
    let returnObject = {'status': '', 'change': []};
    let totalID = 0;
    for (let i = 0; i < cid.length; i++){
      totalID += cid[i][1];
      totalID = Number(totalID.toFixed(2));
    };
    if(totalID < changeToGive){
      returnObject['status'] = 'INSUFFICIENT_FUNDS';
      return returnObject;
    }
    if(totalID > changeToGive){
      returnObject['status'] = 'OPEN';
    }
    if(totalID == changeToGive){
      returnObject['status'] = 'CLOSED';
      // return returnObject;
    }
    // console.log(totalID);
    // console.log(changeToGive);
    // console.log(cid)
    for(let item in values){
      let divisible = Math.floor(changeToGive/values[item])
      if (divisible > 0){
        for(let coin in cid){
          if (cid[coin][0] == item){
            let counter = 0;
            while(counter < divisible && cid[coin][1] >= values[item]){
                cid[coin][1] -= values[item];
                cid[coin][1] = cid[coin][1].toFixed(2)
                // console.log(cid[coin][1]);
                // console.log(values[item]);
                counter++;
            }
            returnObject['change'].push([item,counter*values[item]]);
            // console.log(counter, values[item])
            changeToGive -= counter*values[item];
            changeToGive = changeToGive.toFixed(2)
            // console.log(changeToGive)
          }
        }
      }
    }
    if(returnObject['status'] == 'CLOSED'){
      let tempArr = [];
      for(let i = 0; i < returnObject['change'].length;i++){
        tempArr.unshift(returnObject['change'][i]);
      }
      returnObject['change'] = cid;
      returnObject['change'][0] = tempArr[0];
    }
    if(changeToGive > 0){
      returnObject['status'] = 'INSUFFICIENT_FUNDS';
      returnObject['change'] = [];
    }
    console.log(totalID);
    console.log(changeToGive);
    // console.log(cid)
    // console.log(returnObject)
    return returnObject;
  }
  
  console.log(checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));