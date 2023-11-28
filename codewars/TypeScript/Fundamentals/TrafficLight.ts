export function updateLight(current: string): string {
    const colors = ['green', 'yellow', 'red']
    const currentIndex = colors.indexOf(current)

    if (currentIndex === -1) {
        return `ERROR on ${current}`;
    }

    console.log((currentIndex + 1) % colors.length)
    const nextIndex = (currentIndex + 1) % colors.length;
    return colors[nextIndex];
}

console.log(updateLight('green'))