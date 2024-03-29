const productContainers = [...document.querySelectorAll('.product-container')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];

//скрипт кнопок
productContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;
  
    nxtBtn[i].addEventListener('click', () => {
      const scrollAmount = containerWidth;
      const scrollDuration = 500;
  
      smoothScroll(item, scrollAmount, scrollDuration);
    });
  
    preBtn[i].addEventListener('click', () => {
      const scrollAmount = -containerWidth;
      const scrollDuration = 500;
  
      smoothScroll(item, scrollAmount, scrollDuration);
    });
  });
  
function smoothScroll(element, scrollAmount, duration) {
    const start = element.scrollLeft;
    const startTime = performance.now();
  
    function step(timestamp) {
      const currentTime = timestamp - startTime;
      const scrollProgress = Math.min(currentTime / duration, 1);
      const scrollPosition = start + scrollAmount * scrollProgress;
  
      element.scrollLeft = scrollPosition;
  
      if (currentTime < duration) {
        window.requestAnimationFrame(step);
      }
    }
  
    window.requestAnimationFrame(step);
}