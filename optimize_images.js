const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const imgDir = path.join(__dirname, 'assets', 'images');

// Function to get all files in directory recursively
function getAllFiles(dirPath, arrayOfFiles) {
  const files = fs.readdirSync(dirPath);
  arrayOfFiles = arrayOfFiles || [];
  
  files.forEach(function(file) {
    if (fs.statSync(dirPath + "/" + file).isDirectory()) {
      arrayOfFiles = getAllFiles(dirPath + "/" + file, arrayOfFiles);
    } else {
      arrayOfFiles.push(path.join(dirPath, "/", file));
    }
  });
  return arrayOfFiles;
}

const allFiles = getAllFiles(imgDir);
const imageFiles = allFiles.filter(f => f.match(/\.(jpg|jpeg|png)$/i));

async function processImages() {
  for (const file of imageFiles) {
    const ext = path.extname(file);
    const webpFile = file.replace(new RegExp(ext + '$', 'i'), '.webp');
    
    // Check if webp already exists
    if (!fs.existsSync(webpFile)) {
      try {
        console.log(`Converting ${path.basename(file)} to WebP...`);
        await sharp(file)
          .webp({ quality: 80 })
          .toFile(webpFile);
        
        // Update references in all HTML files
        const htmlFiles = fs.readdirSync(__dirname).filter(f => f.endsWith('.html'));
        for (const htmlFile of htmlFiles) {
          let content = fs.readFileSync(path.join(__dirname, htmlFile), 'utf8');
          // Relative path used in HTML
          const relativeOldPath = file.replace(__dirname + path.sep, '').replace(/\\/g, '/');
          const relativeNewPath = webpFile.replace(__dirname + path.sep, '').replace(/\\/g, '/');
          
          if (content.includes(relativeOldPath) || content.includes(path.basename(file))) {
              const regex = new RegExp(path.basename(file).replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g');
              content = content.replace(regex, path.basename(webpFile));
              fs.writeFileSync(path.join(__dirname, htmlFile), content, 'utf8');
              console.log(`Updated reference in ${htmlFile}`);
          }
        }
      } catch (err) {
        console.error(`Error processing ${file}: ${err.message}`);
      }
    }
  }
  console.log("Image optimization complete!");
}

processImages();
