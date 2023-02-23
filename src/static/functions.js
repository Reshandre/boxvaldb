console.log('function.js')
const handleAlerts = (type,msg)=>{
    alertBox.innerHTML = `
    <div class="alert alert-${type}" role="alert">
      ${msg}
    </div>
    `
}