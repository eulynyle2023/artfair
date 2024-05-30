document.addEventListener('DOMContentLoaded', function () {
  function setupImageUpload(uploadAreaId, fileInputId, previewContainerId) {
      const fileInput = document.getElementById(fileInputId);
      const previewContainer = document.getElementById(previewContainerId);
      const uploadArea = document.getElementById(uploadAreaId);

      // Trigger file input click when the upload area is clicked
      uploadArea.addEventListener('click', function () {
          fileInput.click();
      });

      // Handle file input change event to display the image preview
      fileInput.addEventListener('change', function () {
          const file = this.files[0];
          displayImagePreview(file, previewContainer);
      });

      // Handle drag-and-drop events
      uploadArea.addEventListener('dragover', function (e) {
          e.preventDefault();
          e.stopPropagation();
          uploadArea.classList.add('dragover');
      });

      uploadArea.addEventListener('dragleave', function (e) {
          e.preventDefault();
          e.stopPropagation();
          uploadArea.classList.remove('dragover');
      });

      uploadArea.addEventListener('drop', function (e) {
          e.preventDefault();
          e.stopPropagation();
          uploadArea.classList.remove('dragover');
          
          const files = e.dataTransfer.files;
          if (files.length > 0) {
              const file = files[0];
              displayImagePreview(file, previewContainer);
              fileInput.files = files; // Set the files to the file input
          }
      });
  }

  function displayImagePreview(file, previewContainer) {
      if (file) {
          const reader = new FileReader();

          reader.addEventListener('load', function () {
              const previewImage = document.createElement('img');
              previewImage.setAttribute('src', this.result);
              previewImage.setAttribute('class', 'img-thumbnail');
              previewImage.setAttribute('style', 'max-width: 200px; margin-top: 10px;');

              // Clear the previous preview
              previewContainer.innerHTML = '';
              previewContainer.appendChild(previewImage);
          });

          reader.readAsDataURL(file);
      }
  }

  // Setup image upload boxes
  setupImageUpload('uploadArea1', 'photoUpload1', 'uploadPreview1');
  setupImageUpload('uploadArea2', 'photoUpload2', 'uploadPreview2');
  setupImageUpload('uploadArea3', 'photoUpload3', 'uploadPreview3');
});
