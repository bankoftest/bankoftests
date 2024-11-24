document.addEventListener("DOMContentLoaded", () => {
    const langSwitcher = document.querySelector(".lang-switcher");
    if (langSwitcher) {
        // Detect the current language from the URL or <html> tag
        const currentLang = document.documentElement.lang || "en";
        const baseUrl = window.location.origin + window.location.pathname;

        // Generate links for language switching
        const langLinks = {
            en: baseUrl.replace('/zh/', '/en/'),
            zh: baseUrl.replace('/en/', '/zh/')
        };

        // Update the language switcher
        langSwitcher.innerHTML = `
            <a href="${langLinks.en}" class="${currentLang === 'en' ? 'active' : ''}">English</a> |
            <a href="${langLinks.zh}" class="${currentLang === 'zh' ? 'active' : ''}">中文</a>
        `;
    }
});