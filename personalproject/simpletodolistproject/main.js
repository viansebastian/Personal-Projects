const ITEMS_CONTAINER = document.getElementById('items');
const ITEM_TEMPLATE = document.getElementById('itemTemplate')
const ADD_BUTTON = document.getElementById('add');

let items = getItems();

function getItems(){
    const value = localStorage.getItem('todo') || "[]";

    // return the empty array from json to js array
    return JSON.parse(value)    
}

function setItems(items){
    const itemsJson = JSON.stringify(items); 

    localStorage.setItem('todo', itemsJson); 
}

function addItem(){
    items.unshift({
        description: "", 
        completed: false
    });

    setItems(items);
    refreshList();
}

function refreshList(){
    //TODO: sort items 

    ITEMS_CONTAINER.innerHTML = "";

    for (const item of items) {
        const itemElement = ITEM_TEMPLATE.content.cloneNode(true);
        const descriptionInput = itemElement.querySelector(".item-description");
        const completedInput = itemElement.querySelector(".item-completed");

        descriptionInput.value = item.description;
    }
}


console.log(items);