function doLike(element) {
    const url = element.dataset.url;
    const icon = element.querySelector('i');
    const countElement = element.querySelector('.like-count');
    const articleItem = element.closest('.article-item');

    fetch(url, { method: 'POST' })
        .then(res => res.json())
        .then(data => {
            let currentCount = parseInt(countElement.innerText);
            if (data.liked) {
                element.classList.add('has-text-primary');
                icon.classList.replace('far', 'fas');
                currentCount++;
            } else {
                element.classList.remove('has-text-primary');
                icon.classList.replace('fas', 'far');
                currentCount--;
            }

            countElement.innerText = currentCount;
            if(articleItem){
                articleItem.dataset.likes = currentCount;
            }

        })
        .catch(err => console.error("Error:", err));
}

document.addEventListener('DOMContentLoaded', () => {

    document.querySelectorAll('.js-expand-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const parentColumn = btn.closest('.column');
            const description = parentColumn.querySelector('.content');
            const btnText = btn.querySelector('span:not(.icon)');

            description.classList.toggle('is-hidden');
            btnText.innerText = description.classList.contains('is-hidden') ? 'Zobrazit popis' : 'Skrýt popis';
        });
    });

    const sortSelector = document.getElementById('sort-selector');
    if (sortSelector) {
        sortSelector.addEventListener('change', function() {
            const stream = document.querySelector('.article-stream');
            const articles = Array.from(stream.querySelectorAll('.article-item'));
            const sortBy = this.value;

            articles.sort((a, b) => {
                if (sortBy === 'likes') {
                    return parseInt(b.dataset.likes) - parseInt(a.dataset.likes);
                } else {
                    return parseFloat(b.dataset.timestamp) - parseFloat(a.dataset.timestamp);
                }
            });

            articles.forEach(article => stream.appendChild(article));
        });
    }
});