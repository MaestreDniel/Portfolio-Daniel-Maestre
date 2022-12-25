import { createI18n } from "vue-i18n";
import es from "./es";
import en from "./en";

const messages = {
  es,
  en
};

const spainLangs = ["ca", "eu", "gl"];

// User browser language
const userLocale = window.navigator.userLanguage || window.navigator.language;

const getLocale = lang => {
  if (spainLangs.includes(lang)) {
    return "es";
  }
  return Object.keys(messages).includes(lang) ? lang : "es";
};

const locale = getLocale(userLocale.substring(0, 2));

const i18n = createI18n({
  locale,
  fallbackLocale: process.env.VUE_APP_I18N_FALLBACK_LOCALE,
  silentTranslationWarn: true,
  messages
});

export default i18n;