
var div = document.createElement('div');
 
 
if ('draggable' in div || ('ondragstart' in div && 'ondrop' in div))
    console.log("Drag and Drop API is supported!");