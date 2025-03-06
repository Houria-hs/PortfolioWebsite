

const Observer = new IntersectionObserver((entries)=>{
    entries.forEach((entry)=>{
        console.log(entry)
        if(entry.isIntersecting){
            entry.target.classList.add('show');
        }else{
            entry.target.classList.remove('show');
        }
    });
});

const hiddenElimnets = document.querySelectorAll('.hidden');
hiddenElimnets.forEach((el) => Observer.observe(el));