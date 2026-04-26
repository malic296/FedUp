function openShareModal(uuid) {
    const shareUrl = `${window.location.origin}/article/${uuid}`;

    const modal = document.getElementById('share-modal');
    const input = document.getElementById('share-link-input');
    const copyBtn = document.getElementById('copy-btn');
    const feedback = document.getElementById('copy-feedback');

    input.value = shareUrl;

    copyBtn.innerText = "Kopírovat";
    copyBtn.classList.remove('is-success');
    copyBtn.classList.add('is-link');
    feedback.classList.add('is-hidden');

    modal.classList.add('is-active');
}

function closeShareModal() {
    document.getElementById('share-modal').classList.remove('is-active');
}

function copyShareLink() {
    const input = document.getElementById('share-link-input');
    const copyBtn = document.getElementById('copy-btn');
    const feedback = document.getElementById('copy-feedback');

    navigator.clipboard.writeText(input.value).then(() => {
        copyBtn.innerText = "Zkopírováno!";
        copyBtn.classList.remove('is-link');
        copyBtn.classList.add('is-success');
        feedback.classList.remove('is-hidden');

        setTimeout(() => {
            closeShareModal();
        }, 1500);
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}