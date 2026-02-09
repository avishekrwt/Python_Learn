// @ts-check
/**
 * Generates a random starship registry number.
 *
 * @returns {string} the generated registry number.
 */
export function randomShipRegistryNumber() {
    let lic = Math.floor(Math.random()*(9000)+1000);
    return `NCC-${lic}`;
}

/**
 * Generates a random stardate.
 *
 * @returns {number} a stardate between 41000 (inclusive) and 42000 (exclusive).
 */
export function randomStardate() {
  return Math.random()*1000+41000
}

/**
 * Generates a random planet class.
 *
 * @returns {string} a one-letter planet class.
 */
export function randomPlanetClass() {
  const pclass = "DHJKLMNRTY"
  return pclass[Math.floor(Math.random()*pclass.length)];
}
