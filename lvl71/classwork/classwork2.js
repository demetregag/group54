function removeChildElement() {
    let parent = document.getElementById("parentDiv");
    let child = document.getElementById("childDiv");
    if (parent && child) {
    parent.removeChild(child);
    }
}