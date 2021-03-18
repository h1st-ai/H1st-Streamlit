
import os
import sys
from pathlib import Path

class DigitClassificationService:
    def __init__(self):
        # Setup path
        cur_path = os.path.dirname(os.path.realpath(__file__))
        path_obj = Path(cur_path)
        sys.path.append(str(path_obj))
        sys.path.append(str(path_obj.parent))
        sys.path.append(str(path_obj.parent.parent))

        # Initial workflow
        from workflow import DigitClassificationWorkflow
        self.ai_workflow = DigitClassificationWorkflow()

    async def __call__(self, request):
        from api.utils import preprocess_drawn_image
        try:
            form = await request.form()
            input_img = preprocess_drawn_image(form["upload_file"].file, (28,28))

            results = self.ai_workflow.predict({'X': input_img})["classification"][0]

            return {"prediction": int(results)}
        except Exception as e:
            print(e)
            return {
                "success": False,
                "error": e
            }
