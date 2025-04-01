(deftheme nordic-electric-ai
  "Nordic Electric AI theme inspired by Freyja and Dima.")

(let ((class '((class color) (min-colors 89)))
      (bg "#151e33")
      (fg "#d6e5ff")
      (cursor "#3b9eff")
      (selection "#264F78")
      (comment "#616E88")
      (keyword "#81A1C1")
      (string "#A3BE8C")
      (variable "#D8DEE9")
      (number "#B48EAD")
      (function "#88C0D0")
      (type "#5df0b0"))

  (custom-theme-set-faces
   'nordic-electric-ai
   `(default ((,class (:background ,bg :foreground ,fg))))
   `(cursor ((,class (:background ,cursor))))
   `(region ((,class (:background ,selection))))
   `(font-lock-comment-face ((,class (:foreground ,comment :slant italic))))
   `(font-lock-keyword-face ((,class (:foreground ,keyword :weight bold))))
   `(font-lock-string-face ((,class (:foreground ,string))))
   `(font-lock-variable-name-face ((,class (:foreground ,variable))))
   `(font-lock-constant-face ((,class (:foreground ,number))))
   `(font-lock-function-name-face ((,class (:foreground ,function))))
   `(font-lock-type-face ((,class (:foreground ,type :weight semi-bold))))
   `(fringe ((,class (:background ,bg))))
   `(mode-line ((,class (:background ,selection :foreground ,fg))))
   `(minibuffer-prompt ((,class (:foreground ,keyword :weight bold))))
   ))

(provide-theme 'nordic-electric-ai)